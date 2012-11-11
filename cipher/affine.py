#!/usr/bin/env python3
#-*-coding:utf-8-*-

from itertools import permutations
from sys import exit
import core


class Affine(core.Cipher):
    """This class makes research on afinne chipers."""

    def encrypt(self, message, a, b, lang='en'):
        transposition = {}
        if len(options.lang) > 0:
            lang = options.lang
        if lang == 'en':
            for i in range(26):
                transposition[self.chr(i, lang)] = self.chr((a * i + b) % 26, lang)
            return ''.join(transposition[char] for char in message)
        elif lang == 'ru':
            for i in range(31):
                transposition[self.chr(i, lang)] = self.chr((a * i + b) % 26, lang)
            return ''.join(transposition[char] for char in message)

    def decrypt(self, message, a, b, lang='en'):
        transposition = {}
        if len(options.lang) > 0:
            lang = options.lang
        if lang == 'en':
            for i in range(26):
                transposition[self.chr(i, lang)] = self.chr((core.negative(a, 26) * (i - b)) % 26, lang)
            return ''.join(transposition[char] for char in message)
        elif lang == 'ru':
            for i in range(31):
                transposition[self.chr(i, lang)] = self.chr((core.negative(a, 26) * (i - b)) % 26, lang)
            return ''.join(transposition[char] for char in message)

    def guess(self, sample, lang='en'):
        G = []
        high5 = [self.statistic(sample)[i][0] for i in range(10)]
        H = permutations(high5, 2)
        for h in H:
            x = self.ord(h[0])
            y = self.ord(h[1])
            if lang == 'en':
                x_t = self.ord('e')
                y_t = self.ord('t')
                a = ((x + y) * core.negative(x_t + y_t, 26)) % 26
                b = (x - x_t * a) % 26
            G.append([a, b])
        return G


def main():
    if options.task == "d" or options.task == "decrypt":
        if options.file:
            message = open(options.file, 'r').readlines()
        elif options.a and options.b and options.file:
            message = open(options.file, 'r').readlines()
            text = decrypt(message, options.a, options.b)
            print(text)
            exit(0)
        else:
            sample = open('sample/affine')
        a = Afinne(sample)
        a.set_lang('en')
        a.sample(a.message)
        a.statistic(a.sample)
        hypotesa = a.guess(a.sample, a.statistic)
        print('''
Trying to guess factors (a, b) in [y=a*x+b] equation:
-------------------------------------------------
| i  | guess                          | a  | b  |
-------------------------------------------------''')
        i = 0
        for h in hypotesa:
            dec = a.decrypt(a.sample, h[0], h[1], a.lang)
            i += 1
            print('| {0} | {1} | {2} | {3} |'.format(i, dec[:30], h[0], h[1]))
        print('-------------------------------------------------')
    elif options.task == "e" or options.task == "encrypt":
        if options.a and options.b and options.file:
            message = sample(open(options.file, 'r').readlines())
            text = encrypt(message, options.a, options.b)
            print(text)
            exit(0)
        else:
            print("This task needs more actions.")
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

