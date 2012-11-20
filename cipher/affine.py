#!/usr/bin/env python3
#-*-coding:utf-8-*-

from itertools import permutations
from optparse import OptionParser
from os import curdir
from sys import exit
import core

class Affine(core.Cipher):
    """
    This class makes research on afinne chipers.
    """

    def encrypt(self, a, b):
        n = len(self.alphabet)
        transposition = {}
        for i in range(n):
            transposition[self.chr(i)] = self.chr((a * i + b) % n)
        return ''.join(transposition[char] for char in self.sample)

    def decrypt(self, a, b):
        n = len(self.alphabet)
        transposition = {}
        for i in range(n):
            transposition[self.chr(i)] = self.chr(
                    (core.negative(a, n) * (i - b)) % n)
        return ''.join(transposition[char] for char in self.sample)

    def guess(self, n):
        high = [self.statistic[i][0] for i in range(n)]
        G = []
        H = []
        for h in permutations(high, 2):
            x = self.ord(h[0])
            y = self.ord(h[1])
            if self.language == 'en':
                x_t = self.ord('E')
                y_t = self.ord('T')
                a = ((x + y) * core.negative(x_t + y_t, 26)) % 26
                b = (x - x_t * a) % 26
            G.append([a, b])
        for h in G:
            H.append(self.decrypt(h[0], h[1]), h[0], h[1])
        return H

    def decipher(self):
        hypotesa = self.guess(5)
        print('Trying to guess factors (a, b) in [y=a*x+b] equation:')
        print('|  i | guess                          |  a |  b |')
        print('-------------------------------------------------')
        for h in hypotesa:
            print 
        variant = int(input('Which guess seems to be right? ')) - 1
        while not 0 <= variant <= len(hypotesa):
            print('There are no such variant!')
            variant = int(input('Which guess seems to be right? ')) - 1
        print('Here is open text: {0}'.format(
            self.decrypt(hypotesa[variant][0], hypotesa[variant][1])))
        return (self.decrypt(hypotesa[variant][0], hypotesa[variant][1]), 
                hypotesa[variant][0], 
                hypotesa[variant][1] )

def main():
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
    if options.filename:
        a = Affine(open(options.filename).readlines())
        if options.encrypt:
            if options.a and options.b:
                print(a.encrypt(options.a, options.b))
                exit(0)
            else:
                print("This task needs more actions.")
                exit(0)
        elif options.decrypt:
            if options.a and options.b:
                print(a.decrypt(options.a, options.b))
                exit(0)
            else:
                a.decipher()


if __name__ == '__main__':
    #main()
    a = Affine(open('{0}/../sample/affine'.format(curdir)).readlines())
    a.guess()

