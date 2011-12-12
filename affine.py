#!/usr/bin/env python
#-*-coding:utf-8-*-

from itertools import izip, permutations
from algo import _chr, _ord, negative
import re


class Cipher(object):
    """This class makes research on afinne chipers."""

    __slots__ = ('_message', '_sample', '_statistic', '_lang')

    def __init__(self, info):
        """Transform raw message into models.

        With execution Cipher(X, Y) possible X types is file and array.
        """
        if type(info) is file:
            self._message = info.readlines()
        if type(info) in (str, list):
            self._message = info

    @property
    def message(a):
        return a._message

    @property
    def sample(a):
        return a._sample

    @property
    def statistic(a):
        return a._statistic

    @property
    def lang(a):
        return a._lang

    def set_lang(self, value):
        self._lang = value

    def decrypt(self, message, a, b, lang):
        transposition = {}
        if lang != '':
            if lang == 'en':
                for i in range(26):
                    transposition[_chr(i, lang)] = _chr((a * i + b) % 26, lang)
                return ''.join(transposition[char] for char in message)
            elif lang == 'ru':
                for i in range(31):
                    transposition[_chr(i, lang)] = _chr((a * i + b) % 26, lang)
                return ''.join(transposition[char] for char in message)
        else:
            if options.lang == 'en':
                for i in range(26):
                    transposition[_chr(i, lang)] = _chr((a * i + b) % 26, lang)
                return ''.join(transposition[char] for char in message)

    def guess(self, sample, statistic):
        G = []
        high5 = [statistic[i][0] for i in range(10)]
        H = permutations(high5, 2)
        for h in H:
            x = _ord(h[0])
            y = _ord(h[1])
            if self._lang == 'en':
                x_t = _ord('e')
                y_t = _ord('t')
                a = ((x + y) * negative(x_t + y_t, 26)) % 26
                b = (x - x_t * a) % 26
            if self._lang == 'ru':
                pass
            G.append([a, b])
        return G

    def count_statistic(self, encrypted_message):
        '''Count how many times each char found in message.'''
        stat = {}
        for string in encrypted_message:
            for char in string:
                if char in stat.keys():
                    stat[char] += 1
                else:
                    stat[char] = 1
        self._statistic = sorted(stat.items(), key = lambda x:x[1], reverse = True)

    def create_sample(self, message):
        '''Remove all whitespaces and transform letters into lower case.'''
        text = ''
        sample = ''
        for line in message:
            line = re.sub(re.compile('\s'), '', line)
            sample += line
        for char in sample:
            if options.lang == 'en':
                if 64 < ord(char) < 91:
                    char = chr(ord(char) + 32)
                    text = text + char
                elif 96 < ord(char) < 123:
                    text = text + char
        self._sample = sample

    def sauna_check(crypted_message):
        '''
        You know something about L. S. Kazarin? No?
        Then just forget about this function.
        '''
        for i in range(0, len(crypted_message) - 6):
            for (x1, x2, x5) in izip(crypted_message[i],
                                     crypted_message[i - 1:],
                                     crypted_message[i - 4:]):
                if x2 == x5:
                    x2 = x5 = 'a'
                else:
                    return 0

def main():
    #pass
    #if options.file:
        #sample = create_sample(open(options.file, 'r').readlines())
        #if options.a and options.b:
            #print decrypt(sample, options.a, options.b)
        #elif options.stat:
            #for item in statistic(sample):
                #print str(item[0]) + ' => ' + str(item[1])
        #else:
            #print guess(sample, statistic)
    f = open('file')
    a = Cipher(f)
    a.set_lang('en')
    a.create_sample(a.message)
    a.count_statistic(a.sample)
    hypotesa = a.guess(a.sample, a.statistic)
    print hypotesa
    print a.statistic
    #i = 1
    #for h in hypotesa:
        #print '%d. %s' % (i, a.decrypt(a.sample, h[0], h[1], a.lang)[:30])
        #i += 1
    i = 1
    for h in hypotesa:
        dec = a.decrypt(a.sample, h[0], h[1], a.lang)
        i += 1
        if dec[0] == 'S':
            print '%s: %d %d with %d' % (dec[:30], h[0], h[1], i)


from optparse import OptionParser
parser = OptionParser('usage: %prog [options] [file]')
parser.add_option('-f',
                  dest = 'file',
                  action = 'store',
                  default = '',
                  help = 'decrypt file with given arguments')
parser.add_option('-a',
                  dest = 'a',
                  action = 'store',
                  default = '',
                  help = 'the "a" in y = ax + b equation')
parser.add_option('-b',
                  dest = 'b',
                  action = 'store',
                  default = '',
                  help = 'the "b" in y = ax + b equation')
parser.add_option('-s',
                  dest = 'stat',
                  action = 'store_true',
                  default = False,
                  help = 'perform statistic counting')
parser.add_option('-l',
                  dest = 'lang',
                  action = 'store',
                  default = '',
                  help = 'message language')
(options, args) = parser.parse_args()


if __name__ == '__main__':
    main()

