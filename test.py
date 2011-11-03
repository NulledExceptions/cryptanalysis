#!/usr/bin/env python
#-*-coding:utf-8-*-


import unittest
import os
import affine


affine_crypted = '''
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

class chipers(unittest.TestCase):
    def test_affine_guess(self):
        affine.options.verbose = False
        self.assertEqual(("SAUNA ISNOT KNOWN TOBEA", 17,  7),
                          affine.guess(affine_crypted))

    def test_affine_decrypt(self):
        affine.options.verbose = False
        self.assertEqual("SAUNA ISNOT KNOWN TOBEA",
                         affine.decrypt(affine_crypted, 17, 7))


def main():
    unittest.main()
    return  0


if __name__ == '__main__':
    main()

