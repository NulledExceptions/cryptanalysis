#!/usr/bin/env python3
#-*-coding:utf-8-*-

from cipher import affine, core
import unittest

class affine_test(unittest.TestCase):
    def test_affine_encrypt(self):
        a = affine.Affine('ATTACK AT DAWN')
        self.assertEqual('EJJEKIEJNESR',
                a.encrypt(3, 4)[:20])

    def test_affine_decrypt(self):
        a = affine.Affine('EJJEKIEJNESR')
        self.assertEqual('ATTACKATDAWN',
                a.decrypt(3, 4)[:20])

    def test_affine_decipher(self):
        ciphertext = open('sample/affine').readlines()
        a = affine.Affine(ciphertext)
        x = a.decipher()
        self.assertEqual(('SAUNAISNOTKNOWNTOBEA', 8, 7), 
                (x[0][:20], x[1], x[2]))

class core_test(unittest.TestCase):
    ciphertext = open('sample/affine').readlines()
    a = core.Cipher(ciphertext)

    def test_sampler(self):
        self.assertEqual('BHJUHNBULSVULRUSLYXH',
                         self.a.sample[:20])

if __name__ == '__main__':
    unittest.main()

