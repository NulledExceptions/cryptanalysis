#!/usr/bin/env python3
#-*-coding:utf-8-*-
import cipher.linguistics as linguistics
import builtins
import re

class cached_property(object):
    '''
    A read-only @property that is only evaluated once. 
    The value is cached on the object itself rather than the function 
    or class; this should prevent memory leakage.
    '''
    def __init__(self, func):
        self.func = func

    def __get__(self, instance, cls=None):
        result = instance.__dict__[self.func.__name__] = self.func(instance)
        return result

class Cipher(builtins.str):
    '''
    '''
    def __new__(cls, message, language = None):
        obj = str.__new__(cls, message)
        if type(message) in (builtins.list, builtins.tuple, builtins.str):
            if type(message) in (builtins.list, builtins.tuple):
                message = [string.rstrip() for string in message]
                message = ''.join(str(message))
        else: 
            raise TypeError('Message should be text.')
        if not language:
            language = linguistics.define_language(message)
        obj.message = message
        obj.language = language
        return obj

    def __repr__(self):
        representation = ""
        position = 0
        for c in self.sample:
            if position % 55 == 0:
                representation += '\n'
            elif position % 5 == 0:
                representation += " "
            position += 1
            representation += c
        return representation

    def __str__(self):
        return self.sample

    @cached_property
    def alphabet(self):
        '''
        S.alphabet -> list

        Return alphabet of estimated language.
        '''
        alphabet = list(linguistics.language_list[self.language].keys())
        alphabet.remove('kappa')
        alphabet.remove('max')
        alphabet.sort()
        return alphabet

    @cached_property
    def statistic(self):
        '''
        S.statistic -> list

        Count how many times each char found in message.
        '''
        stat = {}
        for char in self.sample:
            if char in self.alphabet:
                if char in stat.keys():
                    stat[char] += 1
                else:
                    stat[char] = 1
        return sorted(stat.items(), key = lambda x:x[1], reverse = True)

    @cached_property
    def dictionary(self):
        '''
        S.dictionary -> tuple

        List of words in selected language.
        '''
        words = linguistics.get_dictionary(self.language)
        return words

    @cached_property
    def sample(self):
        '''
        Remove all whitespaces and transform letters into lower case.
        '''
        sample = re.sub(re.compile('\s'), '', self.message)
        sample = [char.upper() for char in sample 
               if char.upper() in self.alphabet]
        return ''.join(sample)

    @cached_property
    def language(self):
        '''
        Remove all whitespaces and transform letters into lower case.
        '''
        if not self.language:
            language = 'en'
        return language

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

    def ord(self, char):
        '''
        S.ord(s) -> int

        Return s position in the S natural alphabet.
        Also, says "goodbye" to possible additional info :(
        '''
        if char.upper() in self.alphabet:
            return self.alphabet.index(char.upper())
        return char

    def chr(self, n):
        '''
        S.ord(i) -> str

        Negative for self.ord().
        Return char for i position of S alphabet.
        '''
        if builtins.str(n).isdecimal() and 0 <= n < len(self.alphabet):
            return self.alphabet[n]
        return n

    def istext(self, text = None):
        if not text:
            text = self.message
        text = text.split(' ')
        positive = 0
        for word in text:
            letters = [letter.lower() for letter in word 
                    if letter.capitalize() in self.alphabet]
            word = ''.join(letters)
            if word in self.dictionary:
                positive += 1
        return positive / len(text)

    def define_language(self, text = None):
        if not text:
            text = self.message
        pass

    def isalpha(self, char):
        if char in self.alphabet:
            return True
        return False

