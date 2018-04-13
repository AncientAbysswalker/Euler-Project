# -*- coding: utf-8 -*-
"""
Created on Sat Mar 24

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

#Is the number pandigital?
def isPandigital(number):
	check=len(str(number))
	if check>9:
		raise ValueError('A number cannot exceed 9 pandigital by definition')
	
	if set(str(number)) == set(str(i) for i in range(1,check+1)):
		return True
	return False

#Generate Sets
primes=primeFile()
maxPan=0

#Search primes for L/R trunkable
for p in primes:
	if isPandigital(p) and p>maxPan:
		maxPan=p
		
print(maxPan)
		
	
	