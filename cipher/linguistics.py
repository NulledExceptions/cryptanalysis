#!/usr/bin/env python
#-*- coding: utf-8 -*-
#import builtins
import os
import math

'''
The following are language-specific data on character frequencies.
* kappa is the "index of coincidence"
  [link](http://en.wikipedia.org/wiki/Index_of_coincidence)
* max is the maximum frequency
* languages represented by ISO 639-1:2002 codes
  [link](http://en.wikipedia.org/wiki/ISO_639-1)
'''
language_list = { 
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
      
        'ru' : 
            { 'А':8.04, 'К': 3.49, 'Х':1.02, 
              'Б':1.55, 'Л': 4.32, 'Ц':0.58, 
              'В':4.75, 'М': 3.11, 'Ч':1.23, 
              'Г':1.88, 'Н': 6.72, 'Ш':0.55, 
              'Д':2.95, 'О':10.61, 'Щ':0.34, 
              'Е':8.21, 'П': 2.82, 'Ъ':0.03, 
              'Ё':0.22, 'Р': 5.38, 'Ы':1.91, 
              'Ж':0.80, 'С': 5.71, 'Ь':1.39, 
              'З':1.61, 'Т': 5.83, 'Э':0.31, 
              'И':7.98, 'У': 2.28, 'Ю':0.63, 
              'Й':1.36, 'Ф': 0.41, 'Я':2.00, 
              'max':10.61,
              'kappa':0.0776 },

        'fr' :
            { 'A':8.11, 'À':8.11, 'Â':8.11, 'Æ':8.11, 
              'B':0.91, 'C':3.49, 'Ç':3.49, 'D':4.27, 
              'E':17.22, 'É':17.22, 'È':17.22, 'Ê':17.22, 
              'Ë':17.22, 'F':1.14, 'G':1.09, 'H':0.77, 
              'I':7.44, 'Î':7.44, 'Ï':7.44, 'J':0.34, 
              'K':0.09, 'L':5.53, 'M':2.89, 'N':7.46, 
              'O':5.38, 'Ô':5.38, 'Œ':5.38, 'P':3.02, 
              'Q':0.99, 'R':7.05, 'S':8.04, 'T':6.99, 
              'U':5.65, 'Ù':5.65, 'Û':5.65, 'Ü':5.65, 
              'V':1.30, 'W':0.04, 'X':0.44, 'Y':0.27, 
              'Ÿ':0.27, 'Z':0.09, 
              'max':17.22, 
              'kappa':0.0746 },
      
        'de' :
            { 'A':6.50, 'Ä':6.50, 'B':2.56, 'C':2.83, 
              'D':5.41, 'E':16.69, 'F':2.04, 'G':3.64,
              'H':4.06, 'I':7.81, 'J':0.19, 'K':1.87, 
              'L':2.82, 'M':3.00, 'N':9.90, 'O':2.28, 
              'Ö':2.28, 'P':0.94, 'Q':0.05, 'R':6.53, 
              'S':6.76, 'T':6.74, 'U':3.70, 'Ü':3.70, 
              'V':1.06, 'W':1.39, 'X':0.02, 'Y':0.03, 
              'Z':1.00, 
              'max':16.69, 
              'kappa':0.0767 },
      
        'it' :
            { 'A':11.30, 'À':11.30, 'B':0.97, 'C':4.35, 
              'D':3.80, 'E':11.24, 'É':17.22, 'È':17.22,
              'F':1.09, 'G':1.73, 'H':1.02, 'I':11.57, 
              'Ì':11.57, 'Í':11.57, 'Î':11.57, 'J':0.03, 
              'K':0.07, 'L':6.40, 'M':2.66, 'N':7.29, 
              'O':9.11, 'Ò':9.11, 'Ó':9.11, 'P':2.89, 
              'Q':0.39, 'R':6.68, 'S':5.11, 'T':6.76, 
              'U':3.18, 'Ù':3.18, 'Ú':3.18, 'V':1.52, 
              'W':0.00, 'X':0.02, 'Y':0.048, 'Z':0.95, 
              'max':11.57, 
              'kappa':0.0733 },
        }

def get_dictionary(lang):
    '''
    '''
    curdir = os.path.abspath(os.path.dirname(__file__))
    d = open('{0}/dict/{1}.dictionary'.format(curdir, lang))
    words = d.readlines()
    d.close()
    words = [word.rstrip().lower() for word in words]
    return tuple(words)

def define_language(text):
    '''
    '''
    distribution = { langcode:0 for langcode in language_list.keys() }
    length = 0
    for letter in text:
        for langcode in language_list.keys():
            if letter.upper() in language_list[langcode]:
                distribution[langcode] += 1
                length += 1
    for langcode in distribution.keys():
        if distribution[langcode] > 0:
            distribution[langcode] /= length
    maximum = sorted(distribution.values(), reverse=True)[0]
    # TODO "Core-based" definition.
    if distribution['en'] == maximum:
        return 'en'
    else:
        for langcode in distribution.keys():
            if distribution[langcode] == maximum:
                return langcode

# TODO КОСТЫЛЬ!!!11
def gramm(lang = 'en'):
    ngrams = {}
    curdir = os.path.abspath(os.path.dirname(__file__))
    for line in open('{0}/ngram/{1}.4'.format(curdir, lang)).readlines():
        key, count = line.split(' ') 
        ngrams[key] = int(count)
    N = sum(ngrams.values())
    floor = math.log10(0.01 / N)
    for key in ngrams.keys():
        ngrams[key] = math.log10(float(ngrams[key]) / N)
    return (ngrams, floor)

def istext_4gramms(text, ngr, lang = 'en'):
    '''
    '''
    ngrams, floor = ngr
    score = 0
    for i in range(len(text) - 5):
        if text[i: i + 4] in ngrams: 
            score += ngrams[text[i: i + 4]]
        else: 
            score += floor          
    return score

if __name__ == "__main__":
    pass

