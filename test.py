#!/usr/bin/env python3
#-*-coding:utf-8-*-

import unittest
from cipher import caesar, affine, core

class affine_test(unittest.TestCase):
    ct = open('sample/affine')
    a = core.Cipher(ct.readlines())
    ct.close()

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
    ct = open('sample/affine')
    a = core.Cipher(ct.readlines())
    ct.close()

    def test_caesar_encrypt(self):
        a = caesar.Caesar('ATTACK AT DAWN')
        self.assertEqual('DWWDFN DW GDZQ',
                a.encrypt(3)[:20])

    def test_caesar_decrypt(self):
        a = caesar.Caesar('DWWDFNDWGDZQ')
        self.assertEqual('ATTACKATDAWN',
                a.decrypt(3)[:20])


class core_test(unittest.TestCase):
    ct = open('sample/affine')
    a = core.Cipher(ct.readlines())
    ct.close()

    def test_sampler(self):
        sample = 'BHJUHNBULSVULRUSLYXHONUUNBWNUAXUSNLDYJSSWXRLKGNBONUUNBWSWXKXHKXDHUZDLKXBHJUHBNUONUMHUGSWHUXMBXRWXKXLUXBHJUHCXKXAXKZSWKXXLKOLJKCXLCMXONUUBVULRRWHSHBHJUHNBXMBXRWXKXNOZLJBXXHBNFUBHJUHLUSWXGLLKZLJPHUULSYXBJKXSWHSSWXKXNBHBHJUHYXWNUGSWXGLLK'
        self.assertEqual(sample, self.a.sample)

    def test_representation(self):
        reprsentation = '''
BHJUH NBULS VULRU SLYXH ONUUN BWNUA XUSNL DYJSS WXRLK GNBON UUNBW
SWXKX HKXDH UZDLK XBHJU HBNUO NUMHU GSWHU XMBXR WXKXL UXBHJ UHCXK
XAXKZ SWKXX LKOLJ KCXLC MXONU UBVUL RRWHS HBHJU HNBXM BXRWX KXNOZ
LJBXX HBNFU BHJUH LUSWX GLLKZ LJPHU ULSYX BJKXS WHSSW XKXNB HBHJU
HYXWN UGSWX GLLK'''
        self.assertEqual(reprsentation, self.a.__repr__())

    def test_statistic(self):
        statistic = [
                ('X', 32), ('U', 29), ('H', 23), ('B', 19), 
                ('L', 19), ('N', 16), ('K', 15), ('S', 15), 
                ('W', 14), ('J', 11), ('O', 6), ('R', 6), 
                ('G', 5), ('M', 4), ('Y', 4), ('Z', 4), 
                ('C', 3), ('D', 3), ('A', 2), ('V', 2), 
                ('F', 1), ('P', 1) ]
        self.assertEqual(statistic, self.a.statistic)


if __name__ == '__main__':
    unittest.main()

