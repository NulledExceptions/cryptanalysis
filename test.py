#!/usr/bin/env python3
#-*-coding:utf-8-*-

import unittest
from cipher import caesar, affine, core

class affine_test(unittest.TestCase):
    def test_affine_encrypt(self):
        a = affine.Affine('ATTACK AT DAWN')
        self.assertEqual('EJJEKI EJ NESR', a.encrypt(3, 4))

    def test_affine_decrypt(self):
        a = affine.Affine('EJJEKI EJ NESR')
        self.assertEqual('ATTACK AT DAWN', a.decrypt(3, 4))

    def test_affine_decipher_spaces(self):
        a = affine.Affine('EJJEKI EJ NESR')
        self.assertEqual(('ATTACK AT DAWN', 3, 4), a.decipher())

    def test_affine_decipher_nospaces(self):
        a = affine.Affine('EJJEKIEJNESR')
        self.assertEqual(('ATTACK AT DAWN', 3, 4), a.decipher())


class caesar_test(unittest.TestCase):
    def test_caesar_encrypt(self):
        a = caesar.Caesar('ATTACK AT DAWN')
        self.assertEqual('DWWDFN DW GDZQ', a.encrypt(3))

    def test_caesar_decrypt(self):
        a = caesar.Caesar('DWWDFNDWGDZQ')
        self.assertEqual('ATTACKATDAWN', a.decrypt(3))


class core_test(unittest.TestCase):
    def test_sampler(self):
        a = core.Cipher('Attack at dawn, people!!!1')
        sample = 'ATTACKATDAWNPEOPLE'
        self.assertEqual(sample, a.sample)

    def test_representation(self):
        a = core.Cipher('Attack at dawn, people!!!1')
        reprsentation = '''
ATTAC KATDA WNPEO PLE'''
        self.assertEqual(reprsentation, a.__repr__())

    def test_statistic(self):
        a = core.Cipher('Attack at dawn, people!!!1')
        statistic = [
            ('A', 4), ('T', 3), ('E', 2), ('P', 2), 
            ('C', 1), ('D', 1), ('K', 1), ('L', 1), 
            ('O', 1), ('N', 1), ('W', 1) ]
        self.assertEqual(statistic, a.statistic)


if __name__ == '__main__':
    unittest.main()

