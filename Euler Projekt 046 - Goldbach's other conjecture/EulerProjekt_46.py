# -*- coding: utf-8 -*-
"""
Created on Sat Apr 21

@author: Abysswalker
"""

from os import path
from math import floor,sqrt

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

def conjecture(composite, primes):
	for p in reversed(list(x for x in primes if x < composite)):
		i=sqrt((composite-p)/2)
		if  i == floor(i):
			return True
	return False


#Vars
uLim=10**4 #Upper limit of real numbers toi search for the conjecture failure
primes=primeFile()
primes=set(x for x in primes if x < uLim) #Cap primes set at uLim

#This conmvoluted for generates a set of odd composites by removing primes and evens
for odd_comp in set(range(2,uLim)).difference(primes.union(range(2,uLim,2))):
	if not conjecture(odd_comp,primes):
		print(odd_comp)
		break
	
	