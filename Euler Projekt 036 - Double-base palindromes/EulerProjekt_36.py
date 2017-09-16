# -*- coding: utf-8 -*-
"""
Created on Aug 29

@author: Abysswalker
"""

from math import floor 

def isPalindrome(number):
	number=str(number)
	for digit in range(0,floor(len(number)/2)):
		if number[digit] != number[-1-digit]:
			return False
	return True

sumPalin=0

for numbers in range(1,1000000):
	if isPalindrome(numbers) and isPalindrome(bin(numbers)[2:]):
		sumPalin+=numbers
		
print(sumPalin)