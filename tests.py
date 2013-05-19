#!/usr/bin/env python3
#-*-coding:utf-8-*-
from cipher.classic import caesar, affine, vigenere
import unittest
import cipher


#class affine_test(unittest.TestCase):
    #def test_affine_encrypt(self):
        #a = affine.Affine('ATTACK AT DAWN')
        #self.assertEqual('EJJEKI EJ NESR', a.encrypt(3, 4))

    #def test_affine_decrypt(self):
        #a = affine.Affine('EJJEKI EJ NESR')
        #self.assertEqual('ATTACK AT DAWN', a.decrypt(3, 4))

    #def test_affine_decipher_withspaces(self):
        #a = affine.Affine('EJJEKI EJ NESR')
        #self.assertEqual(('ATTACK AT DAWN', 3, 4), a.decipher())

    #def test_affine_decipher_nospaces(self):
        #a = affine.Affine('EJJEKIEJNESR')
        #self.assertEqual(('ATTACKATDAWN', 3, 4), a.decipher())


#class caesar_test(unittest.TestCase):
    #def test_caesar_encrypt(self):
        #a = caesar.Caesar('ATTACK AT DAWN')
        #self.assertEqual('DWWDFN DW GDZQ', a.encrypt(3))

    #def test_caesar_decrypt(self):
        #a = caesar.Caesar('DWWDFNDWGDZQ')
        #self.assertEqual('ATTACKATDAWN', a.decrypt(3))

    #def test_affine_decipher_russian(self):
        #a = caesar.Caesar('Фэзыя йз зьи ахлш пвёнлш чугрщцкфнлш дцосн, жг еютзм ъгб.')
        #self.assertEqual(('СЪЕШЬ ЖЕ ЕЩЁ ЭТИХ МЯГКИХ ФРАНЦУЗСКИХ БУЛОК, ДА ВЫПЕЙ ЧАЮ.', 3), a.decipher())

    #def test_affine_decipher_english(self):
        #a = caesar.Caesar('QEB NRFZH YOLTK CLU GRJMP LSBO QEB IXWV ALD')
        #self.assertEqual(('THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG', 23), a.decipher())


#class vigenere_test(unittest.TestCase):
    #def test_vigenere_encrypt(self):
        #a = vigenere.Vigenere('ATTACKATDAWN')
        #self.assertEqual('LXFOPVEFRNHR', a.encrypt('LEMON'))

    #def test_vigenere_decrypt(self):
        #a = vigenere.Vigenere('LXFOPVEFRNHR')
        #self.assertEqual('ATTACKATDAWN', a.decrypt('LEMON'))


class classic_core_test(unittest.TestCase):
    def test_sampler(self):
        a = cipher.classic.core('Attack at dawn, people!!!1')
        sample = 'ATTACKATDAWNPEOPLE'
        self.assertEqual(sample, a.sample)

    def test_representation(self):
        a = cipher.classic.core('Attack at dawn, people!!!1')
        reprsentation = '''\nATTAC KATDA WNPEO PLE'''
        self.assertEqual(reprsentation, a.__repr__())

    def test_statistic(self):
        a = cipher.classic.core('AAAaaa bbBB!<>? ЭЮЯцйд')
        statistic = [ ('A', 6), ('B', 4) ]
        self.assertEqual(statistic, a.statistic())


if __name__ == '__main__':
    unittest.main()

