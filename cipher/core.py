#!/usr/bin/env python3
#-*-coding:utf-8-*-

from random import randint
import cipher.linguistics as linguistics
import builtins
import math
import re
import os


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
        curdir = os.path.abspath(os.path.dirname(__file__))
        d = open('{0}/dict/{1}.dictionary'.format(curdir, self.language))
        words = d.readlines()
        d.close()
        words = [word.rstrip().lower() for word in words]
        return tuple(words)

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



def gcd(a, b):
    '''
    Euclid's Algorithm.
    '''
    while b:
        a, b = b, a % b
    return a

def totient(n):
    '''
    Euler's function:
    Compute the number of positives < n that are relatively prime to n.
    '''
    tot, pos = 0, n - 1
    while pos > 0:
        if gcd(pos, n) == 1: tot += 1
        pos -= 1
    return tot

def jacobi(a, n):
    """
    Jacobi symbol: (a|n).
    """
    if a in range(1):
        return a
    elif a == 2:
        if n % 8 in [3, 5]:
            return -1
        return 1
    elif a % 2 == 0:
        return jacobi(2, n) * jacobi(a // 2, n)
    elif a >= n:
        return jacobi(a % n, n)
    elif a % 4 == 3 and n % 4 == 3:
        return -jacobi(n, a)
    return jacobi(n, a)

def negative(a, m):
    """
    Negative element for element a in field Z_m.
    """
    n = a % m;
    (b, x, y, n) = (m, 1, 0, 0);
    while a != 0:
        n = int(b / a);
        (a, b, x, y) = (b - n * a, a, y - n * x, x);
    return y % m

def _negative(a, m):
    """
    Negative element for element a in field Z_m, where m is prime.
    """
    return a ** (totient(m) - 1) % m

def factors(n):
    '''
    Pollard Rho Brent's factorization algorithm.
    https://comeoncodeon.wordpress.com/2010/09/18/pollard-rho-brent-integer-factorization/
    '''
    def brent(N):
        if N % 2 == 0:
            return 2
        y, c, m = randint(1, N-1), randint(1, N-1), randint(1, N-1)
        g, r, q = 1, 1, 1
        while g == 1:            
            x = y
            for i in range(r):
                y = ((y * y) % N + c) % N
            k = 0
            while (k < r and g == 1):
                ys = y
                for i in range(min(m, r - k)):
                    y = ((y * y) % N + c) % N
                    q = q * (abs(x - y)) % N
                g = gcd(q, N)
                k = k + m
            r = r * 2
        if g == N:
            while True:
                ys = ((ys * ys) % N + c) % N
                g = gcd(abs(x - ys), N)
                if g > 1:
                    break
        return g    
    f = []
    while n != 1:
        d = brent(n)
        n /= d
        f.append(d)
    return f

def f2c(nom, denom):
    '''
    Fraction to continous fraction.
    '''
    r_denoms = []
    c_nom = float(nom)
    c_denom = float(denom)
    while True:
        intpart = 0
        if c_nom > c_denom:
            intpart = math.floor(c_nom / c_denom)
            r_denoms.append(int(intpart))
            if (c_nom / c_denom) - intpart == 0:
                break
            c_nom = c_nom - (c_denom * intpart)
        t = c_nom
        c_nom = c_denom
        c_denom = t
    return r_denoms

