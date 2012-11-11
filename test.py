#!/usr/bin/env python3
#-*-coding:utf-8-*-

import unittest
import core

class affine_test(unittest.TestCase):
    from cipher.affine import Affine
    ciphertext = open('sample/affine').readlines()

    def test_affine_encrypt(self):
        a = Affine(self.ciphertext)
        options.lang = 'en'
        self.assertEqual('bhjuhnbulsvulruslyxh',
                         a.encrypt('saunaisnotknowntobea', 23, 21))

    def test_affine_decrypt(self):
        a = Affine(self.ciphertext)
        options.lang = 'en'
        self.assertEqual('saunaisnotknowntobea',
                         a.decrypt('bhjuhnbulsvulruslyxh', 23, 21))

    def test_affine_decipher(self):
        a = Affine(self.ciphertext)
        options.lang = 'en'
        self.assertEqual(('saunaisnotknowntobea', 23,  21),
                          a.decipher())

class core_test(unittest.TestCase):
    ciphertext = open('sample/affine').readlines()

    def test_sampler(self):
        a = core.Cipher(self.ciphertext)
        self.assertEqual('bhjuhnbulsvulruslyxhonuunbwnuaxusnldyjss',
                         a.sample(self.ciphertext)[:40])

if __name__ == '__main__':
    unittest.main()

