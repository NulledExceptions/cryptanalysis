#!/usr/bin/env python3
#-*- coding: utf-8 -*-
import cipher.linguistics as linguistics
import cipher.classic
import os

class Caesar(cipher.classic.core):
    """
    An implementation of the Caesar cipher.
    """
    def encrypt(self, shift):
        """
        Encipher input (plaintext) using the Caesar cipher and return it
        (ciphertext).
        """
        ciphertext = []
        for char in self.message:
            if char.upper() in self.alphabet:
                pos = self.ord(char)
                ciphertext.append(
                        self.alphabet[(pos + shift) % len(self.alphabet)])
            else:
                ciphertext.append(char)
        return ''.join(ciphertext)

    def decrypt(self, shift):
        """
        Decipher input (ciphertext) using the Caesar cipher and return it
        (plaintext).
        """
        return self.encrypt(-shift)

    def decipher(self):
        '''
        Most effective method.
        '''
        return self.bruteforce()

    def bruteforce(self):
        '''
        Full bruteforce with all keys, there are length of alphabet
        of them.
        '''
        hypotesa = []
        for b in range(0, len(self.alphabet)):
            ot = self.decrypt(b)
            if len(ot) > 100:
                score = linguistics.istext_ngramms(ot, self.trigrams)
            else:
                score = linguistics.istext_ngramms(ot, self.tetragrams)
            hypotesa.append((score, ot, b))
        return max(hypotesa)[1:]

def main():
    from optparse import OptionParser
    parser = OptionParser('usage: ./%prog [options] filename')
    parser.add_option('-a', '--analysis',
                      action = 'store_true', dest = 'analysis', default=True,
                      help = 'make analysis, default action')
    parser.add_option('-e', '--encrypt',
                      metavar="A", 
                      help="encrypt file with A shift")
    parser.add_option('-d', '--decrypt',
                      metavar="A", 
                      help = 'decrypt file with A shift')
    (options, args) = parser.parse_args()

    if len(args) != 1:
        parser.print_help()
    else:
        if os.path.exists(args[0]):
            message = open(args[0]).readlines()
        else:
            message = args[0]
        ct = Caesar(message)
        if options.encrypt or options.decrypt:
            if options.encrypt:
                a = options.encrypt
                message = ct.encrypt(int(a))
            elif options.decrypt:
                (a, b) = options.decrypt.split('x')
                message = ct.decrypt(int(a))
            print(message)
        else:
            print("Analysis...")
            print("Defined language is {0}.".format(ct.language))
            ot = ct.decipher()
            print(ot[0])
            print("Decryption parametres is a={0}.".format(ot[1]))

if __name__ == "__main__":
    main()
