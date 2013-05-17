#!/usr/bin/env python3
#-*-coding:utf-8-*-
import builtins

class core(builtins.str):
    '''
    '''
    def encrypt(self):
        '''
		This method should be overriden in Cipher subclass.
        It contains encyption procedure.
        '''
        raise NotImplemented('Encryption is not implemented.')

    def decrypt(self):
        '''
		This method should be overriden in Cipher subclass.
        It contains decyption procedure.
        '''
        raise NotImplemented('Decryption is not implemented.')

    def decipher(self):
        '''
		This method should be overriden in Cipher subclass.
        Actually, cryptanalysis main line should be stored here.
        '''
        raise NotImplemented('Analysis is not implemented.')
