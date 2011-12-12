#!/usr/bin/env python
#-*-coding:utf-8-*-

from itertools import izip
from algo import _chr
import re


class Cipher:
    """This class makes research on afinne chipers."""

    __slots__ = ('_message', '_sample')
    _message = ''
    _sample = ''

    def __init__(self, info):
        """Transform raw message into models.

        With execution Cipher(X, Y) possible X types is file
        and array.
        """

        if type(info) is file:
            self._message = info.readlines()
        if type(info) in (str, list):
            self._message = info

    @property
    def message(self):
        return self._message

    @property
    def sample(self):
        return self._sample

    @property
    def statistic(self):
        return self._statistic

    @classmethod
    def decrypt(self, a, b, lang = '', text = ''):
        transposition = {}
        if text:
            message = text
        else:
            message = self.text
        if lang != '':
            if lang == 'en':
                for i in range(26):
                    transposition[_chr(i)] = _chr((a * i + b) % 26)
                return ''.join(transposition[char] for char in message)
            elif lang == 'ru':
                for i in range(31):
                    transposition[_chr(i)] = _chr((a * i + b) % 26)
                return ''.join(transposition[char] for char in message)
        else:
            if options.lang == 'en':
                for i in range(26):
                    transposition[_chr(i)] = _chr((a * i + b) % 26)
                return ''.join(transposition[char] for char in message)

    @classmethod
    def guess(sample, statistic):
        return 0

    @classmethod
    def count_statistic(encrypted_message):
        '''Count how many times each char found in message.'''
        stat = {}
        for string in encrypted_message:
            for char in string:
                if char in stat.keys():
                    stat[char] += 1
                else:
                    stat[char] = 1
        return sorted(stat.items(), key = lambda x:x[1], reverse = True)

    @classmethod
    def create_sample(self, message):
        '''Remove all whitespaces and transform letters into lower case.'''
        text = ''
        sample = ''
        print self.message
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

    @classmethod
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
    a.create_sample(a.message)
    print a.sample
    print a.decrypt(12,12,text=a.sample)


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

