#!/usr/bin/env python
#-*-coding:utf-8-*-

russian = ["а", "б", "в", "г", "д", "е", "ж", "з",
           "и", "к", "л", "м", "н", "о", "п", "р",
           "с", "т", "у", "ф", "х", "ц", "ч", "ш",
           "щ", "ь", "ъ", "ы", "э", "ю", "я"]
RUSSIAN = ["А", "Б", "В", "Г", "Д", "Е", "Ж", "З",
           "И", "К", "Л", "М", "Н", "О", "П", "Р",
           "С", "Т", "У", "Ф", "Х", "Ц", "Ч", "Ш",
           "Щ", "Ь", "Ъ", "Ы", "Э", "Ю", "Я"]
english = [chr(x) for x in range(97, 123)]
ENGLISH = [chr(x) for x in range(65, 91)]

def statistic(encrypted_message):
    '''
    Count how many times each char found in message.
    '''
    stat = {}
    for string in encrypted_message:
        for char in string:
            if char in stat.keys():
                stat[char] += 1
            else:
                stat[char] = 1
    return sorted(stat.items(), key = lambda x:x[1], reverse = True)

def euclid(a, b):
    '''
    Euclid's Algorithm.
    '''
    while b:
        a, b = b, a % b
    return a

def totient(n):
    '''
    Euler's function:
    Compute the number of positives < n that are relatively prime to n.
    '''
    tot, pos = 0, n - 1
    while pos > 0:
        if euclid(pos, n) == 1: tot += 1
        pos -= 1
    return tot

def negative(a, m):
    """
    Negative element for element a in field Z_m.
    """
    n = a % m;
    (b, x, y, n) = (m, 1, 0, 0);
    while a != 0:
        n = int(b / a);
        (a, b, x, y) = (b - n * a, a, y - n * x, x);
    return y % m

def _negative(a, m):
    """
    Negative element for element a in field Z_m, where m is prime.
    """
    return a ** (totient(m) - 1) % m

def _ord(char, alphabet = []):
    '''
    Returns position in the natural alphabet.
    Also, says "goodbye" to additional info :(
    '''
    if alphabet != []:
        return alphabet.find(char) + 1
    else:
        if char in english:
            return english.find(char) + 1
        elif char in ENGLISH:
            return ENGLISH.find(char) + 1
        elif char in russian:
            return russian.find(char) + 1
        elif char in RUSSIAN:
            return RUSSIAN.find(char) + 1
        else:
            print "[ERROR] Aliens char detected! it is <%d>." % char
            return 0

def _chr(n, alphabet = []):
    '''
    Negative for _ord().
    '''
    if alphabet != []:
        return alphabet[n]
    else:
        if n in english:
            return english[n] + 1
        elif n in ENGLISH:
            return ENGLISH[n] + 1
        elif n in russian:
            return russian[n] + 1
        elif n in RUSSIAN:
            return RUSSIAN[n] + 1
        else:
            print "[ERROR] No char for %d position found!" % n
            return 0

