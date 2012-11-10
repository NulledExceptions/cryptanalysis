#!/usr/bin/env python
#-*-coding:utf-8-*-

import unittest
import affine

class affine_test(unittest.TestCase):
    chiper = '''
    BHJUH NBULS VULRU SLYXH
    ONUUN BWNUA XUSNL DYJSS
    WXRLK GNBON UUNBW SWXKX
    HKXDH UZDLK XBHJU HBNUO
    NUMHU GSWHU XMBXR WXKXL
    UXBHJ UHCXK XAXKZ SWKXX
    LKOLJ KCXLC MXONU UBVUL
    RRWHS HBHJU HNBXM BXRWX
    KXNOZ LJBXX HBNFU BHJUH
    LUSWX GLLKZ LJPHU ULSYX
    BJKXS WHSSW XKXNB HBHJU
    HYXWN UGSWX GLLK
    '''

    def test_affine_decrypt(self):
        a = affine.Afinne(self.chiper)
        affine.options.lang = 'en'
        self.assertEqual('saunaisnotknowntobea',
                         a.decrypt(23, 21, text='bhjuhnbulsvulruslyxh'))

    def test_sampler(self):
        a = affine.Afinne(self.chiper)
        self.assertEqual('bhjuhnbulsvulruslyxhonuunbwnuaxusnldyjss',
                         a.create_sample(self.chiper[:60]))

    def test_affine_guess(self):
        a = affine.Afinne(self.chiper)
        affine.options.lang = 'en'
        self.assertEqual(('saunaisnotknowntobea', 23,  21),
                          a.guess(self.affine_crypted))

class vigenere_test(unittest.TestCase):
    pass

class enigma_test(unittest.TestCase):
    pass

def main():
    unittest.main()
    return 0

if __name__ == '__main__':
    main()

