#!/usr/bin/env python
#-*-coding:utf-8-*-

russian = ("а", "б", "в", "г", "д", "е", "ж", "з",
           "и", "к", "л", "м", "н", "о", "п", "р",
           "с", "т", "у", "ф", "х", "ц", "ч", "ш",
           "щ", "ь", "ъ", "ы", "э", "ю", "я")


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

def euclid(a,b):
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
        if euclid(pos, n) == 1: tot += 1
        pos -= 1
    return tot

def negative(a,m):
    #TODO : a ** (totient(m) - 1) % m
    n = a % m;
    (b, x, y, n) = (m, 1, 0, 0);
    while a != 0:
        n = int(b / a);
        (a, b, x, y) = (b - n * a, a, y - n * x, x);
    return y % m

def _ord(char):
    '''
    [A-Z] = (65-90)
    [a-z] = (97-122)
    [а-я] = (256-286)
    '''
    try:
        return ord(char)
    except:
        if char in russian:
            return russian.find(char) + 256
        else:
            print "ERROR: Aliens language"
            return 0

def _chr(char):
    '''
    Negative for _ord().
    '''
    try:
        return chr(char)
    except:
        if char in russian:
            return russian.find(char) + 256
        else:
            print "ERROR: Aliens language"
            return 0

