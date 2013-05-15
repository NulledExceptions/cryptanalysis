#!/usr/bin/env python3
#-*- coding: utf-8 -*-
import cipher.classic
import os

class Vigenere(cipher.classic.Cipher):
    """
    An implementation of the Vigenere cipher.
    """
    def encrypt(self, key):
        """
        Encipher input (plaintext) using the Vigenere cipher and return
        it (ciphertext).
        """
        ciphertext = []
        k = 0
        n = len(key)
        for i in range(len(self)):
            p = self[i]
            if p.isalpha():
                ciphertext.append(chr((ord(p) + ord(
                (key[k % n].upper(), key[k % n].lower())[int(p.islower())]
                ) - 2*ord('Aa'[int(p.islower())])) % 26 +
                ord('Aa'[int(p.islower())])))
                k += 1
            else:
                ciphertext.append(p)
        return ''.join(ciphertext)

    def decrypt(self, key):
        """
        Decipher input (ciphertext) using the Vigenere cipher and return
        it (plaintext).
        """
        plaintext = []
        k = 0
        n = len(key)
        for i in range(len(self)):
            c = self[i]
            if c.isalpha():
                plaintext.append(chr((ord(c) - ord(
                (key[k % n].upper(), key[k % n].lower())[int(c.islower())]
                )) % 26 + ord('Aa'[int(c.islower())])))
                k += 1
            else:
                plaintext.append(c)
        return ''.join(plaintext)

if __name__ == '__main__':
    from optparse import OptionParser
    parser = OptionParser('usage: ./%prog [options] filename')
    parser.add_option('-a', '--analysis',
                      action = 'store_true', dest = 'analysis', default=True,
                      help = 'make analysis, default action')
    parser.add_option('-e', '--encrypt',
                      metavar="KEY", 
                      help='encrypt file with KEY as a key')
    parser.add_option('-d', '--decrypt',
                      metavar="KEY", 
                      help = 'decrypt file with  KEY as a key')
    (options, args) = parser.parse_args()

    if len(args) != 1:
        parser.print_help()
    else:
        if os.path.exists(args[0]):
            message = open(args[0]).readlines()
        else:
            message = args[0]
        ct = Vigenere(message)
        if options.encrypt or options.decrypt:
            k = options.encrypt
            if options.encrypt:
                message = ct.encrypt(k)
            elif options.decrypt:
                message = ct.decrypt(k)
            print(message)
        else:
            print("Analysis...")
            print("Defined language is {0}.".format(ct.language))
            ot = ct.decipher()
            print(ot[0])
            print("Decryption parametres is a={0} and b={1}.".format(ot[1], ot[2]))

