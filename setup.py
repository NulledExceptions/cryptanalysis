#!/usr/bin/env python3
# -*- coding: utf-8 -*-
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'name': 'pycry',
    'version': '0.0.1',
    'author': 'Alexey Bednyakov',
    'download_url': 'https://github.com/ch3sh1r/cryptanalysis',
    'author_email': 'ch3sh1r@ya.ru',
    'install_requires': [],
    'packages': ['pycry'], 
    'scripts': [],
    'license': 'GPLv2',
    'description': 'Do some reasearch on cryptoanalysis', 
    'long_description': open('README.md').read(),
}

setup(**config)
