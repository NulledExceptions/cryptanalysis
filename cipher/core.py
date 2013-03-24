#!/usr/bin/env python3
#-*-coding:utf-8-*-

from builtins import str
from random import randint
from math import *
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


class Cipher(str):
    '''
    '''
    def __init__(self, ciphertext, language = 'en'):
        """
        Transform raw message into models.
        With execution Cipher(X, Y) possible X types is file and array.
        """
        self.ciphertext = ciphertext
        self.language = language

    def __repr__(self):
        return self.sample

    def __str__(self):
        rval = ""
        pos = 0
        for c in self.sample:
            if pos % 55 == 0:
                rval += '\n'
            elif pos % 5 == 0:
                rval += " "
            pos += 1
            rval += c
        return rval

    @cached_property
    def alphabet(self):
        '''
        S.alphabet -> list

        Return alphabet of estimated language.
        '''
        alphabet = list(_language[self.language].keys())
        alphabet.remove('kappa')
        alphabet.remove('max')
        return alphabet.sort()

    @cached_property
    def statistic(self):
        '''
        S.statistic -> list

        Count how many times each char found in message.
        '''
        stat = {}
        for string in self.message:
            for char in string:
                if char in stat.keys():
                    stat[char] += 1
                else:
                    stat[char] = 1
        return sorted(stat.items(), key = lambda x:x[1], reverse = True)

    @cached_property
    def sample(self):
        '''
        Remove all whitespaces and transform letters into lower case.
        '''
        message = self.ciphertext
        sample = ''
        for line in message:
            line = re.sub(re.compile('\s'), '', line)
            sample += line
        return sample.upper()

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
        if str(n).isdecimal() and 0 <= n < len(self.alphabet):
            return self.alphabet[n]
        return n

    def isalpha(self, char):
        if char in self.alphabet:
            return True
        return False


'''
The following are language-specific data on character frequencies.
* kappa is the "index of coincidence"
  [link](http://en.wikipedia.org/wiki/Index_of_coincidence)
* max is the maximum frequency
* languages represented by ISO 639-1:2002 codes
  [link](http://en.wikipedia.org/wiki/ISO_639-1)
'''
_language = { 
        'ru' : 
            { 'А':1, 'Б':1, 'В':1, 'Г':1, 'Д':1, 'Е':1, 
              'Ж':1, 'З':1, 'И':1, 'К':1, 'Л':1, 'М':1, 
              'Н':1, 'О':1, 'П':1, 'Р':1, 'С':1, 'Т':1, 
              'У':1, 'Ф':1, 'Х':1, 'Ц':1, 'Ч':1, 'Ш':1, 
              'Щ':1, 'Ь':1, 'Ъ':1, 'Ы':1, 'Э':1, 'Ю':1, 
              'Я':1,
              'max':1,
              'kappa':1 },

        'en' :
            { 'A':8.16, 'B':1.49, 'C':2.78, 'D':4.25, 
              'E':12.70, 'F':2.22, 'G':2.01, 'H':6.09, 
              'I':6.99, 'J':0.15, 'K':0.77, 'L':4.02, 
              'M':2.41, 'N':6.74, 'O':7.50, 'P':1.92, 
              'Q':0.09, 'R':5.99, 'S':6.32, 'T':9.05, 
              'U':2.75, 'V':0.97, 'W':2.36, 'X':0.15, 
              'Y':1.97, 'Z':0.07, 
              'max':12.70, 
              'kappa':0.0667 },
      
        'fr' :
            { 'A':8.11, 'B':0.91, 'C':3.49, 'D':4.27, 
              'E':17.22, 'F':1.14, 'G':1.09, 'H':0.77, 
              'I':7.44, 'J':0.34, 'K':0.09, 'L':5.53, 
              'M':2.89, 'N':7.46, 'O':5.38, 'P':3.02, 
              'Q':0.99, 'R':7.05, 'S':8.04, 'T':6.99, 
              'U':5.65, 'V':1.30, 'W':0.04, 'X':0.44, 
              'Y':0.27, 'Z':0.09, 
              'max':17.22, 
              'kappa':0.0746 },
      
        'de' :
            { 'A':6.50, 'B':2.56, 'C':2.83, 'D':5.41, 
              'E':16.69, 'F':2.04, 'G':3.64, 'H':4.06, 
              'I':7.81, 'J':0.19, 'K':1.87, 'L':2.82, 
              'M':3.00, 'N':9.90, 'O':2.28, 'P':0.94, 
              'Q':0.05, 'R':6.53, 'S':6.76, 'T':6.74, 
              'U':3.70, 'V':1.06, 'W':1.39, 'X':0.02, 
              'Y':0.03, 'Z':1.00, 
              'max':16.69, 
              'kappa':0.0767 },
      
        'it' :
            { 'A':11.30, 'B':0.97, 'C':4.35, 'D':3.80, 
              'E':11.24, 'F':1.09, 'G':1.73, 'H':1.02, 
              'I':11.57, 'J':0.03, 'K':0.07, 'L':6.40, 
              'M':2.66, 'N':7.29, 'O':9.11, 'P':2.89, 
              'Q':0.39, 'R':6.68, 'S':5.11, 'T':6.76, 
              'U':3.18, 'V':1.52, 'W':0.00, 'X':0.02, 
              'Y':0.048, 'Z':0.95, 
              'max':11.57, 
              'kappa':0.0733 },
      
        'pt' :
            { 'A':13.89, 'B':0.98, 'C':4.18, 'D':5.24, 
              'E':12.72, 'F':1.01, 'G':1.17, 'H':0.91, 
              'I':6.70, 'J':0.31, 'K':0.01, 'L':2.76, 
              'M':4.54, 'N':5.37, 'O':10.90, 'P':2.74, 
              'Q':1.06, 'R':6.67, 'S':7.90, 'T':4.63,
              'U':4.05, 'V':1.55, 'W':0.01, 'X':0.27, 
              'Y':0.01, 'Z':0.40, 
              'max':13.89, 
              'kappa':0.0745 },
      
        'es' :
            { 'A':12.09, 'B':1.21, 'C':4.20, 'D':4.65, 'E':13.89,
              'F':0.64, 'G':1.11, 'H':1.13, 'I':6.38, 'J':0.4, 
              'K':0.03, 'L':5.19, 'M':2.86, 'N':7.23, 'O':9.5,
              'P':2.74, 'Q':1.37, 'R':6.14, 'S':7.43, 'T':4.4,
              'U':4.53, 'V':1.05, 'W':0.01, 'X':0.12, 'Y':1.1,
              'Z':0.324, 
              'max':13.89, 
              'kappa':0.0766 },
        }

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

