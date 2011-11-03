#!/usr/bin/env python
#-*-coding:utf-8-*-


def decrypt(crypted_message, a, b):
    return 0

def guess(crypted_message):
    return 0

def main():
    if options.file:
        message = open(options.file).readlines()
        if options.a and options.b:
            print decrypt(message, options.a, options.b)
        else:
            print guess(message)
    return 0


from optparse import OptionParser
parser = OptionParser("usage: %prog [options] [file]")
parser.add_option("-v",
                  action="store_true",
                  dest="verbose",
                  default=False,
                  help="print status messages to stdout")
parser.add_option("-g",
                  dest="file",
                  action="store",
                  default="",
                  help="try to guess right arguments")
parser.add_option("-f",
                  dest="file",
                  action="store",
                  default="",
                  help="decrypt file with given arguments")
parser.add_option("-a",
                  dest="a",
                  action="store",
                  default="",
                  help="the 'a' in 'y = ax + b' equation")
parser.add_option("-b",
                  dest="b",
                  action="store",
                  default="",
                  help="the 'b' in 'y = ax + b' equation")
(options, args) = parser.parse_args()


if __name__ == '__main__':
    main()

