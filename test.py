#!/usr/bin/env python
#-*-coding:utf-8-*-

import unittest
import affine


class affine_cipher(unittest.TestCase):
    def test_affine_decrypt(self):
        affine.options.lang = 'en'
        self.assertEqual('saunaisnotknowntobea',
                         affine.decrypt('bhjuhnbulsvulruslyxh', 23, 21))

    def test_sampler(self):
        self.assertEqual('bhjuhnbulsvulruslyxhonuunbwnuaxusnldyjss',
                         affine.create_sample('''BHJUH NBULS VULRU SLYXH
                                                 ONUUN BWNUA XUSNL DYJSS'''))

    def test_affine_guess(self):
        affine.options.lang = 'en'
        self.assertEqual(('saunaisnotknowntobea', 23,  21),
                          affine.guess(self.affine_crypted))

    def test_affine_sauna(self):
        affine.options.lang = 'en'
        self.assertEqual(('saunaisnotknowntobea', 23,  21),
                         affine.sauna_check(self.affine_crypted))


#BHJUH NBULS VULRU SLYXH
#ONUUN BWNUA XUSNL DYJSS
#WXRLK GNBON UUNBW SWXKX
#HKXDH UZDLK XBHJU HBNUO
#NUMHU GSWHU XMBXR WXKXL
#UXBHJ UHCXK XAXKZ SWKXX
#LKOLJ KCXLC MXONU UBVUL
#RRWHS HBHJU HNBXM BXRWX
#KXNOZ LJBXX HBNFU BHJUH
#LUSWX GLLKZ LJPHU ULSYX
#BJKXS WHSSW XKXNB HBHJU
#HYXWN UGSWX GLLK


def main():
    unittest.main()
    return 0


if __name__ == '__main__':
    main()

