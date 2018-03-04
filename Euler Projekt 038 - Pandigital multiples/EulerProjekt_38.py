# -*- coding: utf-8 -*-
"""
Created on Sun Feb 4

@author: Abysswalker
"""

from math import floor,log

#Is the number pandigital?
def isPandigital(number,check):
	if check>9:
		raise ValueError('A number cannot exceed 9 pandigital by definition')
	
	if len(str(number))==check and set(str(number)) == set(str(i) for i in range(1,9+1)):
		return True
	return False


#Empty Set
check_set = set()


#Starting with 1-digit and moving to 4-digit, multiply by applicable n to find largest 9-pandigital
for k in range(1,10):
	test_string=""
	n=1
	while len(test_string)<9:
		if test_string == 9:
			check_set=check_set|{int(test_string)}
		test_string+=str(n*k)
		n+=1

for k in range(10,10000):
	test_string=""
	for n in range(1,6-floor(log(k,10))):
		test_string+=str(n*k)
	if isPandigital(test_string,9):
		print(test_string,isPandigital(test_string,9))
		check_set=check_set|{int(test_string)}
	
print((check_set))
print(max(check_set))
	
	