# -*- coding: utf-8 -*-
"""
Created on Jul 26

@author: Abysswalker
"""

#I'm just going to cheat a little here :3
import urllib                                       
sock = urllib.request.urlopen('http://primos.mat.br/primeiros_10000_primos.txt') 
htmlSource = sock.read()                            
sock.close() 

primes=[]
for each in htmlSource.split():
	primes.append(int(each))
	
#Start real problem
maxPrimes=0
pab=0
for a in range(-1000,1001):
	for b in range(0,1001):
		print(a,b)
		n=0
		prcnt=0
		while True:
			if n**2+a*n+b in primes:
				prcnt+=1
				n+=1
			else:
				if n>maxPrimes:
					pab=a*b
					maxPrimes=n
				break
			
print(pab)