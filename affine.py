#!/usr/bin/env python
#-*-coding:utf-8-*-

from itertools import izip
import re


def decrypt(encrypted_message, a, b):
    transposition = {}
    decrypted_message = ''
    if options.lang == 'en':
        for i in range(26):
            transposition[chr(i + 97)] = chr(((a * i + b) % 26) + 97)
    for char in encrypted_message:
        decrypted_message = decrypted_message + transposition[char]
    return decrypted_message

def guess(crypted_message):
    return 0

def statistic(encrypted_message):
    '''Count how many times each char found in message.'''
    stat = {}
    for string in encrypted_message:
        for char in string:
            if char in stat.keys():
                stat[char] += 1
            else:
                stat[char] = 1
    return sorted(stat.items(), key = lambda x:x[1], reverse = True)

def create_sample(message):
    '''
    Remove all whitespaces and transform letters into lower case.
    '''
    text = ''
    sample = ''
    for line in message:
        line = re.sub(re.compile('\s'), '', line)
        sample = sample + line
    for char in sample:
        if options.lang == 'en':
            if 64 < ord(char) < 91:
                char = chr(ord(char) + 32)
                text = text + char
            elif 96 < ord(char) < 123:
                text = text + char
    return text

def sauna_check(crypted_message):
    '''
    You know something about L. S. Kazarin? No?
    Then just forget about this function.
    '''
    for i in range(0, len(crypted_message) - 6):
        for (x1, x2, x5) in izip(crypted_message[i],
                                 crypted_message[i - 1:],
                                 crypted_message[i - 4:]):
            if x2 == x5:
                x2 = x5 = 'a'
            else:
                return 0

def main():
    if options.file:
        message = create_sample(open(options.file, 'r').readlines())
        if options.a and options.b:
            print decrypt(message, options.a, options.b)
        elif options.stat:
            for item in statistic(message):
                print str(item[0]) + ' => ' + str(item[1])
        else:
            print guess(message)


from optparse import OptionParser
parser = OptionParser('usage: %prog [options] [file]')
parser.add_option('-f',
                  dest = 'file',
                  action = 'store',
                  default = '',
                  help = 'decrypt file with given arguments')
parser.add_option('-a',
                  dest = 'a',
                  action = 'store',
                  default = '',
                  help = 'the "a" in y = ax + b equation')
parser.add_option('-b',
                  dest = 'b',
                  action = 'store',
                  default = '',
                  help = 'the "b" in y = ax + b equation')
parser.add_option('-s',
                  dest = 'stat',
                  action = 'store_true',
                  default = False,
                  help = 'perform statistic counting')
parser.add_option('-l',
                  dest = 'lang',
                  action = 'store',
                  default = '',
                  help = 'message language')
(options, args) = parser.parse_args()


if __name__ == '__main__':
    main()

