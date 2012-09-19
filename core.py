#!/usr/bin/env python
#-*-coding:utf-8-*-
from random import randint
from math import *

__rus = ["а", "б", "в", "г", "д", "е", "ж", "з",
         "и", "к", "л", "м", "н", "о", "п", "р",
         "с", "т", "у", "ф", "х", "ц", "ч", "ш",
         "щ", "ь", "ъ", "ы", "э", "ю", "я"]
__RUS = ["А", "Б", "В", "Г", "Д", "Е", "Ж", "З",
         "И", "К", "Л", "М", "Н", "О", "П", "Р",
         "С", "Т", "У", "Ф", "Х", "Ц", "Ч", "Ш",
         "Щ", "Ь", "Ъ", "Ы", "Э", "Ю", "Я"]
__eng = [chr(x) for x in range(97, 123)]
__ENG = [chr(x) for x in range(65, 91)]

def statistic(encrypted_message):
    '''
    Count how many times each char found in message.
    '''
    stat = {}
    for string in encrypted_message:
        for char in string:
            if char in stat.keys():
                stat[char] += 1
            else:
                stat[char] = 1
    return sorted(stat.items(), key = lambda x:x[1], reverse = True)

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

def jacobi(a,n):
    """
    Jacobi symbol: (a|n).
    """
    if a == 0:
        return 0
    if a == 1:
        return 1
    if a == 2:
        n8 = n % 8
        if n8 == 3 or n8 == 5:
            return -1
        else:
            return 1
    if a%2 == 0:
        return jacobi(2,n) * jacobi(a//2,n)
    if a >= n:
        return jacobi(a%n,n)
    if a%4 == 3 and n%4 == 3:
        return -jacobi(n,a)
    else:
        return jacobi(n,a)

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

def _ord(char, alphabet = []):
    '''
    Returns position in the natural alphabet.
    Also, says "goodbye" to additional info :(
    '''
    if alphabet != []:
        return alphabet.index(char)
    else:
        if char in __eng:
            return __eng.index(char)
        elif char in __ENG:
            return __ENG.index(char)
        elif char in __rus:
            return __rus.index(char)
        elif char in __RUS:
            return __RUS.index(char)
        else:
            print "[ERROR] Aliens char detected! it is <%d>." % char
            return 0

def _chr(n, lang):
    '''
    Negative for _ord().
    '''
    if lang == 'en':
        return __eng[n-1]
    elif lang == 'ru':
        return __rus[n]
    else:
        print "[ERROR] No char for %d position found!" % n
        return 0

def brent(N):
    '''
    Pollard Rho Brent's factorization algorithm.
    https://comeoncodeon.wordpress.com/2010/09/18/pollard-rho-brent-integer-factorization/
    '''
    if N % 2 == 0:
        return 2
    y,c,m = randint(1, N-1), randint(1, N-1), randint(1, N-1)
    g,r,q = 1,1,1
    while g == 1:            
        x = y
        for i in range(r):
            y = ((y*y)%N+c)%N
        k = 0
        while (k<r and g==1):
            ys = y
            for i in range(min(m,r-k)):
                y = ((y*y)%N+c)%N
                q = q*(abs(x-y))%N
            g = gcd(q,N)
            k = k + m
        r = r*2
    if g==N:
        while True:
            ys = ((ys*ys)%N+c)%N
            g = gcd(abs(x-ys),N)
            if g>1:
                break
    return g    

def factors(n):
    f = []
    while n <> 1:
        d = brent(n)
        n /= d
        f.append(d)
    return f

