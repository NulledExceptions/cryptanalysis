#!/usr/bin/env python3
#-*- coding: utf-8 -*-
import cipher.classic

class Caesar(cipher.classic.Cipher):
    """
    An implementation of the Caesar cipher.
    """
    def encrypt(self, shift):
        """
        Encipher input (plaintext) using the Caesar cipher and return it
        (ciphertext).
        """
        ciphertext = []
        for p in self:
            if p.isalpha():
                ciphertext.append(
                        self.chr((self.ord(p) - self.ord('Aa'[int(p.islower())]) + shift) % 26 + 
                            self.ord('Aa'[int(p.islower())])))
            else:
                ciphertext.append(p)
        return Caesar(''.join(ciphertext))

    def decrypt(self, shift):
        """
        Decipher input (ciphertext) using the Caesar cipher and return it
        (plaintext).
        """
        return self.encrypt(-shift)

    def decipher(self, text):
        pass

if __name__ == "__main__":
    pass

