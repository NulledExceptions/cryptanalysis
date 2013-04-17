#!/usr/bin/env python3
# -*- coding: utf-8 -*-  

# TODO Restore namespace.
try:
    from cipher.core import Cipher
except ImportError:
    from core import Cipher
from random import shuffle,randint,choice  
from copy import copy  

class Enigma(core.Cipher):
    def __init__(self, nocogs,printspecialchars):  
        self.printspecialchars=printspecialchars  
        self.nocogs=nocogs  
        self.cogs=[]  
        self.oCogs=[] # Create backup of original cog positions for reset  
  
        for i in range(0,self.nocogs): # Create cogs  
            self.cogs.append(Cog())  
            self.cogs[i].create()  
            self.oCogs.append(self.cogs[i].transformation)  
  
        # Create reflector  
        refabet=copy(range(0,26))  
        self.reflector=copy(range(0,26))  
        while len(refabet)>0:  
            a=choice(refabet)  
            refabet.remove(a)  
            b=choice(refabet)  
            refabet.remove(b)  
            self.reflector[a]=b  
            self.reflector[b]=a  
  
    def print_setup(self): # To print the enigma setup for debugging/replication  
        print "Enigma Setup:\nCogs: ",self.nocogs,"\nCog arrangement:"  
        for i in range(0,self.nocogs):  
            print self.cogs[i].transformation  
        print "Reflector arrangement:\n",self.reflector,"\n"  
  
    def reset(self):  
        for i in range(0,self.nocogs):  
            self.cogs[i].setcog(self.oCogs[i])  
  
    def encode(self,text):  
        ln=0  
        ciphertext=""  
        for l in text.lower():  
            num=ord(l)%97  
            if (num>25 or num<0):  
                if (self.printspecialchars): # readability  
                    ciphertext+=l  
                else:  
                    pass # security  
            else:  
                ln+=1  
                for i in range(0,self.nocogs): # Move thru cogs forward...  
                    num=self.cogs[i].passthrough(num)  
  
                num=self.reflector[num] # Pass thru reflector  
  
                for i in range(0,self.nocogs): # Move back thru cogs...  
                    num=self.cogs[self.nocogs-i-1].passthroughrev(num)  
                ciphertext+=""+chr(97+num) # add encrypted letter to ciphertext  
  
                for i in range(0,self.nocogs): # Rotate cogs...  
                    if ( ln % ((i*6)+1) == 0 ): # in a ticker clock style  
                        self.cogs[i].rotate()  
        return ciphertext  
  
class Cog():
    '''
    Simple substitution cipher for each cog.
    '''

    def create(self):  
        self.transformation=copy(range(0,26))  
        shuffle(self.transformation)  
        return  

    def passthrough(self,i):  
        return self.transformation[i]  

    def passthroughrev(self,i):  
        return self.transformation.index(i)  

    def rotate(self):  
        self.transformation=shift(self.transformation, 1)  

    def setcog(self,a):  
        self.transformation=a  

def shift(l, n): 
    '''
    Method to rotate arrays/cogs  
    '''
    return l[n:] + l[:n]  
  
if __name__ == "__main__":
    plaintext="""
The most common arrangement used a ratchet and pawl mechanism. 
Each rotor had a ratchet with 26 teeth and, 
every time a key was pressed, each 
of the pawls corresponding to a particular rotor would move 
forward in unison, 
trying to engage with a ratchet, thus stepping the 
attached rotor once. A thin 
metal ring attached to each rotor upon which the pawl 
rode normally prevented 
this. As this ring rotated with its rotor, 
a notch machined into it would 
eventually align itself with the pawl, allowing it to 
drop into position, engage 
with the ratchet, and advance the rotor. The 
first rotor, having no previous 
rotor (and therefore no notched ring controlling a pawl),
stepped with every 
key press. The five basic rotors (I–V)
had one notch each, while the additional 
naval rotors VI, VII and VIII had two notches.
The position of the notch on each 
rotor was determined by the letter ring which could be 
adjusted in relation to 
the core containing the interconnections. The points on the 
rings at which they 
caused the next wheel to move were as follows 

http://www.stealthcopter.com/blog/category/cryptography/
    """  
      
    x=Enigma(4,True)  
    #x.print_setup()  
      
    print "Plaintext:\n"+plaintext+"\n"  
    ciphertext=x.encode(plaintext)  
    print "Ciphertext:\n"+ciphertext+"\n"  
      
# To proove that encoding and decoding are symmetrical  
# we reset the enigma to starting conditions and enter  
# the ciphertext, and get out the plaintext  
    x.reset()  
    plaintext=x.encode(ciphertext)  
    print "Plaintext:\n"+plaintext+"\n"  

