#!/usr/bin/env python
#-*- coding:utf-8 -*-
import random
import math

def gcd(a, b):
    '''Euclid's Algorithm.
    '''
    while b:
        a, b = b, a % b
    return a

def totient(n):
    '''Euler's function:
    Compute the number of positives < n that are relatively prime to n.
    '''
    tot, pos = 0, n - 1
    while pos > 0:
        if gcd(pos, n) == 1: tot += 1
        pos -= 1
    return tot

def jacobi(a, n):
    '''Jacobi symbol: (a|n).
    '''
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
    '''Negative element for element a in field Z_m.
    '''
    n = a % m;
    (b, x, y, n) = (m, 1, 0, 0);
    while a != 0:
        n = int(b / a);
        (a, b, x, y) = (b - n * a, a, y - n * x, x);
    return y % m

def _negative(a, m):
    '''Negative element for element a in field Z_m, where m is prime.
    '''
    return a ** (totient(m) - 1) % m

def factors(n):
    '''Pollard Rho Brent's factorization algorithm.
    https://comeoncodeon.wordpress.com/2010/09/18/pollard-rho-brent-integer-factorization/
    '''
    def brent(N):
        if N % 2 == 0:
            return 2
        y, c, m = random.randint(1, N-1), random.randint(1, N-1), random.randint(1, N-1)
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
    '''Fraction to continous fraction.
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
