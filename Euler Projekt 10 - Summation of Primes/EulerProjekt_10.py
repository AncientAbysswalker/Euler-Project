# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11, 2017

@author: Abysswalker
"""

from functools import reduce

#Check if prime
def isPrime(number,primes):
    for prime in primes:
        if number%prime == 0:
            return False
    return True

#Generate primes up to a limit
def genPrimes(upper):
	primes=[2]
	for natnum in range(2,upper):
		print(natnum)
		if isPrime(natnum,primes):
			primes.append(natnum)
	return primes

#Main
primes=genPrimes(2000000)
a=reduce(lambda x, y: x + y, primes)

print(a)