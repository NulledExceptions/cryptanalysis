#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# ---------------------------------------------------------------
# Author: hellman ( hellman1908@gmail.com )
# License: GNU GPL v2 ( http://opensource.org/licenses/gpl-2.0.php )
# ---------------------------------------------------------------
from args import parse_parameters, ArgError
from routine import *
import string
import math
import sys
import os

DIRNAME = 'xor_output'
PARAMETERS = dict()

def main():
    global PARAMETERS
    try:
        PARAMETERS = parse_parameters()
        ciphertext = get_ciphertext()
        update_key_length(ciphertext)

        if  PARAMETERS["brute_chars"] != None:
            try_chars = range(0,256)
        elif PARAMETERS["brute_printable"] != None:
            try_chars = map(lambda x : ord(x), string.printable)
        elif PARAMETERS["most_frequent_char"] != None:
            try_chars = [PARAMETERS["most_frequent_char"]]
        else:
            print("Most possible char is needed to guess the key!")
            sys.exit(0)
        
        (probable_keys, key_char_used) = guess_probable_keys_for_chars(ciphertext, try_chars)
        print_keys(probable_keys)
        produce_plaintexts(ciphertext, probable_keys, key_char_used)

    except IOError as err:
        print("[ERROR] Can't load file:\n\t", err)
    except ArgError as err:
        print("[ERROR] Bad argument:\n\t", err)
    except MkdirError as err:
        print("[ERROR] Can't create directory:\n\t", err)
    else:
        return
    cleanup()

# -----------------------------------------------------------------------------
# LOADING CIPHERTEXT
# -----------------------------------------------------------------------------

def get_ciphertext():
    """
    Load ciphertext from a file or stdin and hex-decode if needed
    """
    ciphertext = load_file(PARAMETERS["filename"])
    if PARAMETERS["input_is_hex"]:
        HEXDIGITS = "0123456789abcdefABCDEF"
        only_hex_digits = "".join([c for c in ciphertext if c in HEXDIGITS])
        ciphertext = only_hex_digits.decode("hex")
    return ciphertext

# -----------------------------------------------------------------------------
# KEYLENGTH GUESSING SECTION
# -----------------------------------------------------------------------------

def update_key_length(text):
    """
    Guess length of the key if it's not set. (Updates PARAMETERS)
    """
    global PARAMETERS
    if PARAMETERS["known_key_length"]:
        return
    PARAMETERS["known_key_length"] = guess_key_length(text)
    return


def guess_key_length(text):
    """
    Try key lengths from 1 to max_key_length and print local maximums.
    Set key_length to the most possible if it's not set by user.
    """
    fitnesses = calculate_fitnesses(text)
    print_fitnesses(fitnesses)
    guess_and_print_divizors(fitnesses)

    return get_max_fitnessed_key_length(fitnesses)


def calculate_fitnesses(text):
    """
    Calc. fitnesses for each keylen
    """
    prev = 0
    pprev = 0
    fitnesses = []
    for key_length in range(1, PARAMETERS["max_key_length"] + 1):
        fitness = count_equals(text, key_length)

        # smaller key-length with nearly the same fitness is preferable
        fitness = float(fitness) / (PARAMETERS["max_key_length"] + key_length ** 1.5)

        if pprev < prev and prev > fitness:  # local maximum
            fitnesses += [(key_length - 1, prev)]

        pprev = prev
        prev = fitness

    return fitnesses


def print_fitnesses(fitnesses):
    print("The most probable key lengths:")

    # top sorted by fitness, but print sorted by length
    fitnesses.sort(key=lambda a: a[1], reverse=True)
    top10 = fitnesses[:10]
    best_fitness = top10[0][1]
    top10.sort(key=lambda a: a[0])

    fitness_sum = calculate_fitness_sum(top10)

    for key_length, fitness in top10:
        s1 = str(key_length).rjust(4, " ")
        s2 = str(round(100 * fitness * 1.0 / fitness_sum, 1)) + "%"
        if fitness == best_fitness:
            print(s1 + ":  " + s2)
        else:
            print(s1 + ":  " + s2)
    return


def calculate_fitness_sum(fitnesses):
    return sum([f for (key_length, f) in fitnesses])


def count_equals(text, key_length):
    """
    count equal chars count for each offset and sum them
    """
    equals_count = 0
    if key_length >= len(text):
        return 0

    for offset in range(key_length):
        chars_count = chars_count_at_offset(text, key_length, offset)
        equals_count += max(chars_count.values()) - 1  # why -1? don't know
    return equals_count


def guess_and_print_divizors(fitnesses):
    """
    Prints common divizors and returns the most common divizor
    """
    divizors_counts = [0 for i in range(PARAMETERS["max_key_length"] + 1)]
    for key_length, fitness in fitnesses:
        for number in range(3, key_length + 1):
            if key_length % number == 0:
                divizors_counts[number] += 1
    max_divizors = max(divizors_counts)

    limit = 3
    ret = 2
    for number, divizors_count in enumerate(divizors_counts):
        if divizors_count == max_divizors:
            print("Key-length can be " + str(number) + "*n")
            ret = number
            limit -= 1
            if limit == 0:
                return ret
    return ret


def get_max_fitnessed_key_length(fitnesses):
    max_fitness = 0
    max_fitnessed_key_length = 0
    for key_length, fitness in fitnesses:
        if fitness > max_fitness:
            max_fitness = fitness
            max_fitnessed_key_length = key_length
    return max_fitnessed_key_length


def chars_count_at_offset(text, key_length, offset):
    chars_count = dict()
    for pos in range(offset, len(text), key_length):
        c = text[pos]
        if c in chars_count:
            chars_count[c] += 1
        else:
            chars_count[c] = 1
    return chars_count

# -----------------------------------------------------------------------------
# KEYS GUESSING SECTION
# -----------------------------------------------------------------------------

def guess_probable_keys_for_chars(text, try_chars):
    """
    Guess keys for list of characters.
    """
    probable_keys = []
    key_char_used = {}

    for c in try_chars:
        keys = guess_keys(text, c)
        for key in keys:
            key_char_used[key] = c
            if key not in probable_keys:
                probable_keys.append(key)

    return (probable_keys, key_char_used)

def guess_keys(text, most_char):
    """
    Generate all possible keys for key length
    and the most possible char
    """
    key_length = PARAMETERS["known_key_length"]
    key_possible_bytes = [[] for i in range(key_length)]

    for offset in range(key_length):  # each byte of key<
        chars_count = chars_count_at_offset(text, key_length, offset)
        max_count = max(chars_count.values())
        for char in chars_count:
            if chars_count[char] >= max_count:
                key_possible_bytes[offset] += chr(ord(char) ^ most_char)

    return all_keys(key_possible_bytes)


def all_keys(key_possible_bytes, key_part="", offset=0):
    """
    Produce all combinations of possible key chars
    """
    keys = []
    if offset >= len(key_possible_bytes):
        return [key_part]
    for c in key_possible_bytes[offset]:
        keys += all_keys(key_possible_bytes, key_part + c, offset + 1)
    return keys


def print_keys(keys):
    if not keys:
        print("No keys guessed!")
        return
    
    s1 = str(len(keys))
    s2 = str(len(keys[0]))
    print("{0} possible key(s) of length {1}:".format(s1, s2))
    for key in keys[:5]:
        print(repr(key)[1:-1])
    if len(keys) > 10:
        print("...")

def percentage_printable(text):
    x = 0.0
    for c in text:
        if c in string.printable:
            x+=1
    return x/len(text)
    
def produce_plaintexts(ciphertext, keys, key_char_used):
    """Produce plaintext variant for each possible key,
    creates csv files with keys, percentage of printable
    characters and used most frequent character
    """
    cleanup()
    mkdir(DIRNAME)

    # this is split up in two files since the
    # key can contain all kinds of characters

    fn_key_mapping = "filename-key.csv"
    fn_perc_mapping = "filename-char_used-perc_printable.csv"

    key_mapping = open(os.path.join(DIRNAME,  fn_key_mapping), "w")
    perc_mapping = open(os.path.join(DIRNAME, fn_perc_mapping), "w")

    key_mapping.write("file_name;key_repr\n")
    perc_mapping.write("file_name;char_used;perc_printable\n")

    threshold_printable = 95
    count_printable = 0

    for index, key in enumerate(keys):
        key_index = str(index).rjust(len(str(len(keys) - 1)), "0")
        key_repr = repr(key)[1:-1].replace("/", "\\x2f")
        if not sys.platform.startswith("linux"):
            key_repr = alphanum(key)
        file_name = os.path.join(DIRNAME, key_index + ".out")

        dexored = dexor(ciphertext, key)
        perc = round(100*percentage_printable(dexored))
        if perc > threshold_printable:
            count_printable += 1
        key_mapping.write("{0};{1}\n".format(file_name, key_repr))
        perc_mapping.write("{0};{1};{2}\n".format(
            file_name, repr(key_char_used[key]), perc))
        f = open(file_name, "wb")
        f.write(dexored)
        f.close()
    key_mapping.close()
    perc_mapping.close()

    s1 = str(count_printable)
    s2 = str(round(threshold_printable))

    print("Found {0} plaintexts with {1}%+ printable characters".format(
        s1, s2))
    print("See files {0}, {1}".format(fn_key_mapping, fn_perc_mapping))
    return

def cleanup():
    if os.path.exists(DIRNAME):
        rmdir(DIRNAME)
    return


if __name__ == "__main__":
    main()
