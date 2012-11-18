#!/usr/bin/env python3
#-*-coding:utf-8-*-

from itertools import permutations
from optparse import OptionParser
from sys import exit
import core

class Affine(core.Cipher):
    """
    This class makes research on afinne chipers.
    """

    def encrypt(self, a, b):
        message = self.sample
        transposition = {}
        lang = self.language
        if lang == 'en':
            for i in range(26):
                transposition[self.chr(i)] = self.chr(
                        (a * i + b) % 26)
            return ''.join(transposition[char] for char in message)
        elif lang == 'ru':
            for i in range(31):
                transposition[self.chr(i)] = self.chr(
                        (a * i + b) % 26)
            return ''.join(transposition[char] for char in message)

    def decrypt(self, a, b):
        message = self.sample
        transposition = {}
        lang = self.language
        if lang == 'en':
            for i in range(26):
                transposition[self.chr(i)] = self.chr(
                        (core.negative(a, 26) * (i - b)) % 26)
            return ''.join(transposition[char] for char in message)
        elif lang == 'ru':
            for i in range(31):
                transposition[self.chr(i)] = self.chr(
                        (core.negative(a, 26) * (i - b)) % 26)
            return ''.join(transposition[char] for char in message)

    def guess(self):
        G = []
        high5 = [self.statistic[i][0] for i in range(5)]
        H = permutations(high5, 2)
        for h in H:
            x = self.ord(h[0])
            y = self.ord(h[1])
            if self.language == 'en':
                x_t = self.ord('e')
                y_t = self.ord('t')
                a = ((x + y) * core.negative(x_t + y_t, 26)) % 26
                b = (x - x_t * a) % 26
            G.append([a, b])
        return G

    def decipher(self):
        print('Trying to guess factors (a, b) in [y=a*x+b] equation:')
        print('-------------------------------------------------')
        print('|  i | guess                          |  a |  b |')
        print('-------------------------------------------------')
        i = 0
        hypotesa = self.guess()
        for h in hypotesa:
            dec = self.decrypt(h[0], h[1])
            i += 1
            print('| {0:-2g} | {1} | {2:-2g} | {3:-2g} |'.format(
                   i, dec[:30], h[0], h[1]))
        print('-------------------------------------------------')
        variant = int(input('Which guess seems to be right? ')) - 1
        while not 0 <= variant <= len(hypotesa):
            print('There is no such variant!')
            variant = int(input('Which guess seems to be right? ')) - 1
        print('Here is open text: {0}'.format(
            self.decrypt(hypotesa[variant][0], hypotesa[variant][1])))

def main():
    if options.filename:
        message = open(options.filename).readlines()
        a = Affine(message)
        if options.encrypt:
            if options.a and options.b:
                print(a.encrypt(options.a, options.b))
                exit(0)
            else:
                print("This task needs more actions.")
                exit(0)
        elif options.decrypt:
            if options.a and options.b:
                a = Affine(message)
                print(a.decrypt(options.a, options.b))
                exit(0)
            else:
                a.decipher()


if __name__ == '__main__':
    parser = OptionParser('usage: python %prog [options] [file]')
    parser.add_option('-d', '--decrypt',
                      action = 'store_false', dest = 'decrypt', default=False,
                      help = 'what task we are going to manage')
    parser.add_option('-e', '--encrypt',
                      action='store_false', dest='encrypt', default=False,
                      help="don't print status messages to stdout")
    parser.add_option('-f', '--file', 
                      dest='filename',
                      help='write report to FILE', metavar='FILE')
    parser.add_option('-a', 
                      dest = 'a', action = 'store',
                      help = 'the "a" in y = ax + b equation')
    parser.add_option('-b', 
                      dest = 'b', action = 'store',
                      help = 'the "b" in y = ax + b equation')
    (options, args) = parser.parse_args()
    main()

