#!/usr/bin/env python
#-*-coding:utf-8-*-

from itertools import izip, permutations
from sys import exit
import core
import re


class Afinne(core.Cipher):
    """This class makes research on afinne chipers."""

    def encrypt(self, message, a, b, lang):
        transposition = {}
        if lang != '':
            if lang == 'en':
                for i in range(26):
                    transposition[_chr(i, lang)] = _chr((a * i + b) % 26, lang)
                return ''.join(transposition[char] for char in message)
            elif lang == 'ru':
                for i in range(31):
                    transposition[_chr(i, lang)] = _chr((a * i + b) % 26, lang)
                return ''.join(transposition[char] for char in message)
        else:
            if options.lang == 'en':
                for i in range(26):
                    transposition[_chr(i, lang)] = _chr((a * i + b) % 26, lang)
                return ''.join(transposition[char] for char in message)

    def decrypt(self, message, a, b, lang):
        transposition = {}
        if lang != '':
            if lang == 'en':
                for i in range(26):
                    transposition[_chr(i, lang)] = _chr((core.negative(a, 26) * (i - b)) % 26, lang)
                return ''.join(transposition[char] for char in message)
            elif lang == 'ru':
                for i in range(31):
                    transposition[_chr(i, lang)] = _chr((core.negative(a, 26) * (i - b)) % 26, lang)
                return ''.join(transposition[char] for char in message)
        else:
            if options.lang == 'en':
                for i in range(26):
                    transposition[_chr(i, lang)] =  _chr((core.negative(a, 26) * (i - b)) % 26, lang)
                return ''.join(transposition[char] for char in message)

    def guess(self, sample, statistic):
        G = []
        high5 = [statistic[i][0] for i in range(10)]
        H = permutations(high5, 2)
        for h in H:
            x = _ord(h[0])
            y = _ord(h[1])
            if self._lang == 'en':
                x_t = _ord('e')
                y_t = _ord('t')
                a = ((x + y) * core.negative(x_t + y_t, 26)) % 26
                b = (x - x_t * a) % 26
            elif self._lang == 'ru':
                pass
            G.append([a, b])
        return G

    def statistic(self, encrypted_message):
        '''Count how many times each char found in message.
        '''
        stat = {}
        for string in encrypted_message:
            for char in string:
                if char in stat.keys():
                    stat[char] += 1
                else:
                    stat[char] = 1
        self._statistic = sorted(stat.items(), key = lambda x:x[1], reverse = True)

    def create_sample(self, message):
        '''Remove all whitespaces and transform letters into lower case.
        '''
        text = ''
        sample = ''
        for line in message:
            line = re.sub(re.compile('\s'), '', line)
            sample += line
        for char in sample:
            if options.lang == 'en':
                if 64 < ord(char) < 91:
                    char = chr(ord(char) + 32)
                    text = text + char
                elif 96 < ord(char) < 123:
                    text = text + char
        self._sample = sample


def main():
    if options.task == "d" or options.task == "decrypt":
        if options.file:
            message = create_sample(open(options.file, 'r').readlines())
        elif options.a and options.b and options.file:
            message = create_sample(open(options.file, 'r').readlines())
            text = decrypt(message, options.a, options.b)
            print text
            exit(0)
        else:
            sample = open('sample/affine')
        a = Afinne(sample)
        a.set_lang('en')
        a.create_sample(a.message)
        a.statistic(a.sample)
        hypotesa = a.guess(a.sample, a.statistic)
        print '''
Trying to guess factors (a, b) in [y=a*x+b] equation:
-------------------------------------------------
| i  | guess                          | a  | b  |
-------------------------------------------------'''
        i = 0
        for h in hypotesa:
            dec = a.decrypt(a.sample, h[0], h[1], a.lang)
            i += 1
            print '| %-2g | %s | %-2g | %-2g |' % (i, dec[:30], h[0], h[1])
        print '-------------------------------------------------'
    elif options.task == "e" or options.task == "encrypt":
        if options.a and options.b and options.file:
            message = create_sample(open(options.file, 'r').readlines())
            text = encrypt(message, options.a, options.b)
            print text
            exit(0)
        else:
            print "This task needs more actions."
            exit(0)


from optparse import OptionParser
parser = OptionParser('usage: python %prog [options] [file]')
parser.add_option('-f',
                  dest = 'file',
                  action = 'store',
                  default = '',
                  help = 'encrypt file with given arguments')
parser.add_option('-a',
                  dest = 'a',
                  action = 'store',
                  default = 'd',
                  help = 'the "a" in y = ax + b equation')
parser.add_option('-b',
                  dest = 'b',
                  action = 'store',
                  default = '',
                  help = 'the "b" in y = ax + b equation')
parser.add_option('-l',
                  dest = 'lang',
                  action = 'store',
                  default = '',
                  help = 'message language')
parser.add_option('-t',
                  dest = 'task',
                  action = 'store',
                  default = '',
                  help = 'what task we are going to manage')
(options, args) = parser.parse_args()


if __name__ == '__main__':
    main()

