# -*- coding: utf-8 -*-
"""
Created on Tue Jul  10

@author: Ancient Abysswalker
"""

from math import pow, floor

def isPrime(number,Primes):
    for Prime in Primes:
        if number%Prime == 0:
            return False
    return True

def genFactors(limit):
	primes=[2]
	factors={}
	
	factors[2]=1
	for i in range(3,limit+1):
		#Append new Primes
		if isPrime(i,primes):
			primes.append(i)
			factors[i]=0
		
		for prime in primes:
			if i%prime==0 and i/prime>factors[prime]:
				factors[prime]=floor(pow(i,1/prime))###WRONG
				#print(factors)
	
	return factors
			

#Problem definition, upperLimit must be >2
upperLimit=20

#Check largest products for first palindrome
product=1
factors=genFactors(upperLimit)
for fct,cnt in factors.items():
	product*=int(pow(fct,cnt))

print(product)
	