#!/usr/bin/env python3
#-*- coding: utf-8 -*-
import cipher.classic
import optparse
import os

class Vigenere(cipher.classic.core):
    """
    An implementation of the Vigenere cipher.
    """
    def encrypt(self, key):
        """
        Encrypt input using the Vigenere cipher.
        """
        encrypt_letter = (lambda m, k: 
            self.chr((self.ord(m) + self.ord(k)) 
                % len(self.alphabet)))
        return self.mapper(encrypt_letter, key)

    def decrypt(self, key):
        """
        Decrypt input using the Vigenere cipher.
        """
        decrypt_letter = (lambda m, k: 
            self.chr((self.ord(m) - self.ord(k) + len(self.alphabet)) 
                % len(self.alphabet)))
        return self.mapper(decrypt_letter, key)

    def mapper(self, f, key):
        '''
        Blur all work except function.
        '''
        key = key.upper()
        for letter in key:
            if letter not in self.alphabet:
                raise ValueError(
                        'Key should be the same language as message.')
        pad = key * (len(self) % len(key))
        complement = key[:len(self) - len(pad)]
        padded_key = pad + complement
        result = map(f, self, padded_key)
        return ''.join(result)

if __name__ == '__main__':
    parser = optparse.OptionParser('usage: ./%prog [options] filename')
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
