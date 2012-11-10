#!/usr/bin/env python
#-*-coding:utf-8-*-

import unittest
import affine
import core

class affine_test(unittest.TestCase):
    ciphertext = file('sample/affine').readlines()

    def test_affine_encrypt(self):
        a = affine.Afinne(self.ciphertext)
        affine.options.lang = 'en'
        self.assertEqual('bhjuhnbulsvulruslyxh',
                         a.encrypt('saunaisnotknowntobea', 23, 21))

    def test_affine_decrypt(self):
        a = affine.Afinne(self.ciphertext)
        affine.options.lang = 'en'
        self.assertEqual('saunaisnotknowntobea',
                         a.decrypt('bhjuhnbulsvulruslyxh', 23, 21))

    def test_affine_decipher(self):
        a = affine.Afinne(self.ciphertext)
        affine.options.lang = 'en'
        self.assertEqual(('saunaisnotknowntobea', 23,  21),
                          a.decipher())

class core_test(unittest.TestCase):
    ciphertext = file('sample/affine').readlines()

    def test_sampler(self):
        a = core.Cipher(self.ciphertext)
        self.assertEqual('bhjuhnbulsvulruslyxhonuunbwnuaxusnldyjss',
                         a.sample(self.ciphertext)[:40])

def main():
    unittest.main()
    return 0

if __name__ == '__main__':
    main()

