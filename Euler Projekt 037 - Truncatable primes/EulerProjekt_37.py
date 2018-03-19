# -*- coding: utf-8 -*-
"""
Created on Fri Oct 6

@author: Abysswalker
"""

from os import path

#Import Primes from file
def primeFile():
	filepath = path.join(path.dirname(__file__),"primes.txt")
	primes=set()
	
	print("Checking existance of generated prime file")
	if not path.exists(filepath):
		raise ValueError("File does not exist, error...")
	else:
		print("File exists, parsing...")
		f=open(filepath, 'r')
		for num in f.read().split():
			primes.add(int(num))
		print("Parsing complete!")
	
	f.close()
	return primes

def trunkableLeft(number,primes):
	for i in range(1,len(str(number))):
		if int(str(number)[:-i]) not in primes:
			return False
	return True

def trunkableRight(number,primes):
	for i in range(1,len(str(number))):
		if int(str(number)[i:]) not in primes:
			return False
	return True


#Generate Sets
excludePrimes = {2,3,5,7}
primes=primeFile()
full_set = set()

#Search primes for L/R trunkable
for p in primes:
	if trunkableLeft(p,primes) and trunkableRight(p,primes) and (p not in excludePrimes):
		full_set=full_set|{p}
		
print(sum(full_set))
		
	
	