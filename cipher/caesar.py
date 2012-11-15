#!/usr/bin/env python
#-*- coding: utf-8 -*-

import core

class Caesar(core.Cipher):
    """
    An implementation of the Caesar cipher.
    """

    def encipher(self, shift):
        """
        Encipher input (plaintext) using the Caesar cipher and return it
        (ciphertext).
        """
        ciphertext = []
        for p in self:
            if p.isalpha():
                ciphertext.append(chr((ord(p) - ord('Aa'[int(p.islower())]) +
                shift) % 26 + ord('Aa'[int(p.islower())])))
            else:
                ciphertext.append(p)
        return Caesar(''.join(ciphertext))

    def decipher(self, shift):
        """
        Decipher input (ciphertext) using the Caesar cipher and return it
        (plaintext).
        """
        return self.encipher(-shift)


if __name__ == "__main__":
    pass

