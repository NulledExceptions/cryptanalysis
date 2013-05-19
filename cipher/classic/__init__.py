#!/usr/bin/env python3
#-*-coding:utf-8-*-
import cipher.linguistics as linguistics
import builtins
import cipher
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

class core(cipher.core):
    '''
    Classical cipher base class.
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
            if position % 55 == 0 and position != 0:
                representation += '\n'
            elif position % 5 == 0 and position != 0:
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
        alphabet = linguistics.language_list[self.language]['alphabet']
        alphabet = [x[0] for x in alphabet]
        return list(alphabet)

    @cached_property
    def alphabet_distribued(self):
        '''
        S.alphabet -> list
        Return alphabet of estimated language.
        '''
        alphabet = linguistics.language_list[self.language]['alphabet']
        distribued = sorted(alphabet, key = lambda x: x[1], reverse = True)
        distribued = [x[0] for x in distribued]
        return distribued

    @cached_property
    def dictionary(self):
        '''
        S.dictionary -> tuple
        List of words in selected language.
        '''
        words = linguistics.get_dictionary(self.language)
        return words
    
    @cached_property
    def monograms(self):
        '''
        S.monograms -> list
        List of monograms for selected language.
        '''
        monograms = linguistics.get_ngramms(1, self.language)
        return monograms

    @cached_property
    def bigrams(self):
        '''
        S.bigrams -> list
        List of bigrams for selected language.
        '''
        bigrams = linguistics.get_ngramms(2, self.language)
        return bigrams

    @cached_property
    def trigrams(self):
        '''
        S.trigrams -> list
        List of trigrams for selected language.
        '''
        trigrams = linguistics.get_ngramms(3, self.language)
        return trigrams

    @cached_property
    def tetragrams(self):
        '''
        S.tetragrams -> list
        List of tetragrams for selected language.
        '''
        tetragrams = linguistics.get_ngramms(4, self.language)
        return tetragrams

    @cached_property
    def sample(self):
        '''
        S.sample -> str
        Remove all whitespaces and transform letters into lower case.
        '''
        sample = re.sub(re.compile('\s'), '', self.message)
        sample = [char.upper() for char in sample if char.upper() in self.alphabet]
        return ''.join(sample)

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
        return sorted(stat.items(), key = lambda x: x[1], reverse = True)

    def ord(self, char):
        '''
        S.ord(c) -> int
        Return c position in the S natural alphabet.
        Negative for self.chr(): S.chr(self.ord(c)) should be c.
        '''
        if char.upper() in self.alphabet:
            return self.alphabet.index(char.upper())
        return char

    def chr(self, n):
        '''
        S.ord(n) -> str
        Return char for n position of S alphabet.
        Negative for self.ord(): S.ord(self.chr(n)) should be n.
        '''
        if builtins.str(n).isdecimal() and 0 <= n < len(self.alphabet):
            return self.alphabet[n]
        return n
