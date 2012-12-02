#!/usr/bin/env python3
#-*-coding:utf-8-*-

try:
    from cipher.core import Cipher, negative
except ImportError:
    from core import Cipher, negative
from itertools import permutations


class Affine(Cipher):
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
                    (negative(a, n) * (i - b)) % n)
        return ''.join(transposition[char] for char in self.sample)

    def guess(self, n = 5):
        high = [self.statistic[i][0] for i in range(n)]
        G = []
        H = []
        for h in permutations(high, 2):
            x = self.ord(h[0])
            y = self.ord(h[1])
            if self.language == 'en':
                x_t = self.ord('E')
                y_t = self.ord('T')
                a = ((x + y) * negative(x_t + y_t, 26)) % 26
                b = (x - x_t * a) % 26
            G.append((a, b))
        for h in G:
            H.append((self.decrypt(h[0], h[1]), h[0], h[1]))
        return H

    def decipher(self, iteration = 0, shift = 0):
        hypotesa = self.guess(5 + iteration)
        print('\nTrying to guess factors (a, b) in [y = a * x + b] equation:')
        print('|  i | guess {0} |  a |  b |'.format(' ' * 44))
        print('-' * 69)
        for i, h in enumerate(hypotesa[shift:]):
            print('| {0:-2g} | {1} | {2:-2g} | {3:-2g} |'.format(
                   i + 1, h[0][:50], h[1], h[2]))

        def communicate(message = ''):
            print(message)
            variant = input(
                  'Which guess seems to be right? [1..{0} or None] '.format(i))
            if variant == '':
                return -1
            elif variant.isalpha():
                if (variant.lower() == 'none' or 
                    variant.lower() == 'n'):
                    return -1
                else:
                    return communicate('It should be number [1..{0}] or None. '.format(i))
            elif variant.isdigit():
                variant = int(variant)
                if 1 <= variant <= len(hypotesa):
                    return variant - 1
                return communicate(
                        'You should choose variant from 1 to {0}.'.format(i))

        desigion = communicate()
        if desigion == -1:
            iteration += 1
            return self.decipher(iteration, i)
        else:
            desigion += shift
            return (self.decrypt(hypotesa[desigion][1], hypotesa[desigion][2]),
                    hypotesa[desigion][1], 
                    hypotesa[desigion][2])


def main():
    from optparse import OptionParser
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
    (options, args) = parser.parse_args()

    if options.filename:
        a = Affine(open(options.filename).readlines())
        if options.encrypt:
            print(a.encrypt(options.a, options.b))
        elif options.decrypt:
            if options.a and options.b:
                print(a.decrypt(options.a, options.b))
            else:
                a.decipher()


if __name__ == '__main__':
    main()

