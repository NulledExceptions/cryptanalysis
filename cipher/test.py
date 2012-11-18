#!/usr/bin/env python3
#-*-coding:utf-8-*-

import unittest

class affine_test(unittest.TestCase):
    import affine
    ciphertext = open('../sample/affine').readlines()
    a = affine.Affine(ciphertext)

    def test_affine_encrypt(self):
        self.assertEqual('bhjuhnbulsvulruslyxh',
                self.a.encrypt(23, 21)[:20])

    def test_affine_decrypt(self):
        import affine
        self.assertEqual('SAUNAISNOTKNOWNTOBEA',
                self.a.decrypt(23, 21)[:20])

    def test_affine_decipher(self):
        self.assertEqual(('SAUNAISNOTKNOWNTOBEA', 23,  21),
                          self.a.decipher())

class core_test(unittest.TestCase):
    import core
    ciphertext = open('../sample/affine').readlines()
    a = core.Cipher(ciphertext)

    def test_sampler(self):
        self.assertEqual('BHJUHNBULSVULRUSLYXHONUUNBWNUAXUSNLDYJSS',
                         self.a.sample[:40])

if __name__ == '__main__':
    unittest.main()

