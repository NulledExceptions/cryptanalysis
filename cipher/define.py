#!/usr/bin/env python3
#-*-coding:utf-8-*-
import os
import itertools
import time
import cipher.linguistics as linguistics
import cipher.routine as routine
import cipher.classic

class Affine(cipher.classic.core):
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

    def decipher(self):
        '''
        '''
        hypotesa = []
        for a in [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23]:
            for b in range(0, len(self.alphabet)):
                ot = self.decrypt(a, b)
                if len(ot) > 100:
                    score = linguistics.istext_ngramms(ot, self.trigrams)
                else:
                    score = linguistics.istext_ngramms(ot, self.tetragrams)
                hypotesa.append((score, ot, a, b))
        return max(hypotesa)[1:]


def main():
    from optparse import OptionParser
    parser = OptionParser('usage: ./%prog [options] filename')
    parser.add_option('-a', '--analysis',
                      action = 'store_true', dest = 'analysis', default=True,
                      help = 'make analysis, default action')
    (options, args) = parser.parse_args()

    if len(args) != 1:
        parser.print_help()
    else:
        if os.path.exists(args[0]):
            message = open(args[0]).readlines()
        else:
            message = args[0]
        ct = Affine(message)
        print("Analysis...")
        time.sleep(5)
        print("Defined cipher is Affine.")
        time.sleep(2)
        print("Defined language is {0}.".format(ct.language))
        ot = ct.decipher()
        print(ot[0])
        print("Decryption parametres is a={0} and b={1}.".format(ot[1], ot[2]))

if __name__ == '__main__':
    main()

