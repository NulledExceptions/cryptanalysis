#!/usr/bin/env python3
#-*-coding:utf-8-*-

from itertools import permutations
import core


class Affine(core.Cipher):
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
                    (core.negative(a, n) * (i - b)) % n)
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
                a = ((x + y) * core.negative(x_t + y_t, 26)) % 26
                b = (x - x_t * a) % 26
            G.append((self.decrypt(a, b), a, b))
        return G

    def decipher(self, iteration = 0, shift = 0):
        '''
        '''
        # Step 1: Bruteforce whith language test.
        # TODO Test words / letters.
        base = range(1, len(self.alphabet) + 1)
        for a in base:
            coprimes = [b for b in base if core.gcd(a, b) == 1]
            for b in coprimes:
                ot = self.decrypt(a, b)
                if self.istext(ot) > 0.7:
                    return (ot, a, b)

        # Step 2: Bruteforce whith viewer test.
        hypotesa = self.guess(5 + iteration)
        print('\nTrying to guess factors (a, b) in [y = a * x + b] equation:')
        print('|  i | guess {0} |  a |  b |'.format(' ' * 44))
        print('-' * 69)
        for i, h in enumerate(hypotesa[shift:]):
            print('| {0:-2g} | {1} | {2:-2g} | {3:-2g} |'.format(
                   i + 1, h[0][:50], h[1], h[2]))

        def communicate(message = ''):
            '''
            '''
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
        ct = Affine(open(args[0]).readlines())
        if options.encrypt or options.decrypt:
            print("Language is {0}.".format(ct.language))
            if options.encrypt:
                #print("Encryption...")
                (a, b) = options.encrypt.split('x')
                message = ct.encrypt(int(a), int(b))
            elif options.decrypt:
                #print("Decryption...")
                (a, b) = options.decrypt.split('x')
                message = ct.decrypt(int(a), int(b))
            for line in eval(message):
                print(line)
        else:
            print("Analysis...")
            print("Language is {0}.".format(ct.language))
            message = ct.decipher()
            for line in eval(message[0]):
                print(line)
            print("Decryption parametres is a={0} and b={1}.".format(message[1], message[2]))


if __name__ == '__main__':
    main()

