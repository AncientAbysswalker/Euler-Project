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
		for num in f.read().split():
			primes.add(int(num))
		print("Parsing complete!")
	
	f.close()
	return primes

def grow_trunkPrime(seed, direction):
	plant={seed}
	num_set=range(1,10)
	prime_set = {3,5,7}
	#left
	if direction==-1:	
		for extra_digit in num_set:
			#print(int(str(extra_digit) + str(seed)))
			temp=int(str(extra_digit) + str(seed))
			if temp in primes:
				#print("falge")
				#plant=plant|grow_trunkPrime(temp,-1)
				for i in range(1,len(str(temp))):
					if int(str(temp)[:-i]) not in primes:
						plant=set()
				plant=plant|grow_trunkPrime(temp,-1)|grow_trunkPrime(temp,1)
				#print(plant)
	if direction==1:	
		for extra_digit in prime_set:
			#print(int(str(seed) + str(extra_digit)))
			temp=int(str(seed) + str(extra_digit))
			if temp in primes:
				#print("falge")
				for i in range(1,len(str(temp))):
					if int(str(temp)[i:]) not in primes:
						plant=set()
				plant=plant|grow_trunkPrime(temp,1)|grow_trunkPrime(temp,-1)
	if plant == {seed}:
		return {seed}
	#print(plant)	
	return plant



#Generate Sets
prime_set = {2,3,5,7}
full_set = set()
global primes
primes = genPrimes(10**9)


print(prime_set)

#Use primes as seeds
for seed in prime_set:
	full_set=full_set|grow_trunkPrime(seed, -1)
	full_set=full_set|grow_trunkPrime(seed, 1)
		
print(full_set)
		
	
	