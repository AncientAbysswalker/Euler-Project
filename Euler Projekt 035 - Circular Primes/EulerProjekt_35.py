# -*- coding: utf-8 -*-
"""
Created on Fri Oct 6

@author: Abysswalker
"""

from os import path

#Is a number prime
def isNewPrime(number,primes):
	for prime in primes:
		if number%prime == 0:
			return False
	return True

#Generate primes up to a limit
def genPrimes(upper):
	filepath = path.join(path.dirname(__file__),"primes.txt")
	primes=set()
	
	print("Checking existance of generated prime file")
	if not path.exists(filepath):
		print("File does not exist, generating...")

		primes.add(2)
		for natnum in range(2,upper):
			if isNewPrime(natnum,primes):
				primes.add(natnum)
		
		f = open(filepath,"w")
		f.write(str(primes)[1:-1])
		print("File generated. Next run of this program should skip this step!")
	else:
		print("File exists, parsing...")
		f=open(filepath, 'r')
		for num in f.read().split(','):
			primes.add(int(num))
		print("Parsing complete!")
	
	f.close()
	return primes

def textrotate(l, n):
	l=str(l)
	return l[-n:] + l[:-n]


#Check if rotations are also prime
circprimes=set()
primes=genPrimes(10**6)
for prime in primes:
	checkprimes=set(int(textrotate(prime,i)) for i in range(len(str(prime))+1))
	if checkprimes < primes:
		print(checkprimes, "are circular")
		primes=primes-checkprimes
		circprimes=circprimes|checkprimes
		
print("There are",len(circprimes),"circular primes below 1000000")
		
	
	