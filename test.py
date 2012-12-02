#!/usr/bin/env python3
#-*-coding:utf-8-*-

import unittest
from cipher import caesar, affine, core

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
        ciphertext = open('sample/affine')
        a = affine.Affine(ciphertext.readlines())
        ciphertext.close()
        x = a.guess()[0]
        self.assertEqual(('SAUNAISNOTKNOWNTOBEA', 8, 7), 
                (x[0][:20], x[1], x[2]))


class caesar_test(unittest.TestCase):
    def test_caesar_encrypt(self):
        a = caesar.Caesar('ATTACK AT DAWN')
        self.assertEqual('DWWDFN DW GDZQ',
                a.encrypt(3)[:20])

    def test_caesar_decrypt(self):
        a = caesar.Caesar('DWWDFNDWGDZQ')
        self.assertEqual('ATTACKATDAWN',
                a.decrypt(3)[:20])


class core_test(unittest.TestCase):
    ciphertext = open('sample/affine')
    a = core.Cipher(ciphertext.readlines())
    ciphertext.close()

    def test_sampler(self):
        self.assertEqual('BHJUHNBULSVULRUSLYXH',
                         self.a.sample[:20])

if __name__ == '__main__':
    unittest.main()

