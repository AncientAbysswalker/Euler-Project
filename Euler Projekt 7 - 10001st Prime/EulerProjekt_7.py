# -*- coding: utf-8 -*-
"""
Created on Tue Jul  10

@author: Ancient Abysswalker
"""

def checkPrime(number,Primes):
    for Prime in Primes:
        if number%Prime == 0:
            return False
    return True

#I'm just going to cheat a little here :3
import urllib                                       
sock = urllib.request.urlopen('http://primos.mat.br/primeiros_10000_primos.txt') 
htmlSource = sock.read()                            
sock.close() 

primes=[]
for each in htmlSource.split():
	primes.append(int(each))
	
#Move up from 10000th prime to find next prime
currentValue=primes[-1]
while True:
	if checkPrime(currentValue,primes):
		break
	else:
		currentValue+=1
print(currentValue)