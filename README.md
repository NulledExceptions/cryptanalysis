Cryptanalysis
=============

All this grown on my deepest love to all kind of math-based algorythms and,
especially, cryptographic ones. Or, if you are fan of the naked truth, on 
fear of nearest test.

The following ciphers are currently being studied:

* [Caesar](http://en.wikipedia.org/wiki/Caesar_cipher) - simpliest 
  pre-historical cipher.
* [Affine](http://en.wikipedia.org/wiki/Affine_cipher) - substitution 
  cipher, studied as abstraction of most shift ciphers.
* [Viginere](http://en.wikipedia.org/wiki/Vigenère_cipher) - polyalphabetic 
  substitution, aesy to uderstand and hard to analyse.

Usage
-----

All files except can be used like executables:

    # Expopt PYTHONPATH
    $ . ./prepare

    # Simple test.
    $ ./cipher/affine.py 'EJJEKI EJ NESR'
    Analysis...
    Defined language is en.
    ATTACK AT DAWN
    Decryption parametres is a=3 and b=4.

    # Encrypting english sample.
    $ ./cipher/affine.py -e 9x23 sample/en.opentext > sample/en.affine

    # Analyzing encrypted.
    $ ./cipher/affine.py sample/en.affine 
    Analysis...
    Defined language is en.
    ['TO BE, OR NOT TO BE: THAT IS THE QUESTION:', 
    # Looong decrypted message ... 
    Decryption parametres is a=9 and b=23.

Also, each file can be used like module:

    $ ipython3
    In [1]: import cipher.affine as a

    In [2]: secret = a.Affine('EJJEKI EJ NESR')

    In [3]: secret
    Out[3]: 
    EJJEK IEJNE SR

    In [4]: secret.statistic
    Out[4]: [('E', 4), ('J', 3), ('R', 1), ('S', 1), ('K', 1), ('I', 1), ('N', 1)]

    In [5]: secret.decipher()
    Out[5]: ('ATTACK AT DAWN', 3, 4)

