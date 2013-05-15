#!/usr/bin/env python3
#-*-coding:utf-8-*-
import os
import cipher.routine as routine
import cipher.linguistics as linguistics
import cipher.alphabetic
from itertools import permutations

class Affine(cipher.alphabetic.Cipher):
    '''
    This class makes research on afinne chipers.
    '''
    def encrypt(self, a, b):
        '''
        '''
        n = len(self.alphabet)
        transposition = {}
        for i in range(n):
            transposition[self.chr(i)] = self.chr((a * i + b) % n)
        ct = ''
        for char in self.message:
            if char.upper() in self.alphabet:
                char = transposition[char.upper()]
            ct += char
        return ct

    def decrypt(self, a, b):
        '''
        '''
        n = len(self.alphabet)
        transposition = {}
        for i in range(n):
            transposition[self.chr(i)] = self.chr(
                    (routine.negative(a, n) * (i - b)) % n)
        ot = ''
        for char in self.message:
            if char.upper() in self.alphabet:
                char = transposition[char.upper()]
            ot += char
        return ot

    def guess(self, n = 5):
        '''
        '''
        high = [self.statistic[i][0] for i in range(n)]
        G = []
        for h in permutations(high, 2):
            x = self.ord(h[0])
            y = self.ord(h[1])
            if self.language == 'en':
                x_t = self.ord('E')
                y_t = self.ord('T')
                a = ((x + y) * routine.negative(x_t + y_t, 26)) % 26
                b = (x - x_t * a) % 26
            G.append((self.decrypt(a, b), a, b))
        return G

    def decipher(self, iteration = 0, shift = 0):
        '''
        '''
        hypotesa = []
        n = len(self.alphabet)
        for a in range(1, n + 1):
            if routine.gcd(a, n) == 1:
                for b in range(1, n + 1):
                    ot = self.decrypt(a, b)
                    score = linguistics.istext_4gramms(ot)
                    hypotesa.append((score, ot, a, b))
        print(hypotesa)
        return max(hypotesa)


def main():
    from optparse import OptionParser
    parser = OptionParser('usage: ./%prog [options] filename')
    parser.add_option('-a', '--analysis',
                      action = 'store_true', dest = 'analysis', default=True,
                      help = 'make analysis, default action')
    parser.add_option('-e', '--encrypt',
                      metavar="AxB", 
                      help="encrypt file with A and B args")
    parser.add_option('-d', '--decrypt',
                      metavar="AxB", 
                      help = 'decrypt file with A and B args')
    (options, args) = parser.parse_args()

    if len(args) != 1:
        parser.print_help()
    else:
        if os.path.exists(args[0]):
            message = open(args[0]).readlines()
        else:
            message = args[0]
        ct = Affine(message)
        if options.encrypt or options.decrypt:
            if options.encrypt:
                (a, b) = options.encrypt.split('x')
                message = ct.encrypt(int(a), int(b))
            elif options.decrypt:
                (a, b) = options.decrypt.split('x')
                message = ct.decrypt(int(a), int(b))
            for line in eval(message):
                print(line)
        else:
            print("Analysis...")
            print("Defined language is {0}.".format(ct.language))
            ot = ct.decipher()
            print(ot[0])
            print("Decryption parametres is a={0} and b={1}.".format(ot[1], ot[2]))

if __name__ == '__main__':
    main()

