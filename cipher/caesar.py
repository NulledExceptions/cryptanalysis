#!/usr/bin/env python3
#-*- coding: utf-8 -*-

# TODO Restore namespace.
try:
    from cipher.core import Cipher
except ImportError:
    from core import Cipher


class Caesar(Cipher):
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


if __name__ == "__main__":
    pass

