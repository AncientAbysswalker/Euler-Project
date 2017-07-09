# -*- coding: utf-8 -*-
"""
Created on Tue Jul  8

@author: Ancient Abysswalker
"""

from math import floor 
   
def isPalindrome(number):
    number=str(number)
    for digit in range(0,floor(len(number)/2)):
        if number[digit] != number[-1-digit]:
            return False
    return True

#Problem definition
maxMult=999
maxPalindrome=0


#Check largest products for first palindrome
for i in reversed(range(80,maxMult+1)):
    #Centric Diagonal
	if (i)*(i)<maxPalindrome:
		print(maxPalindrome)
		break
	for j in range(0,maxMult-i+1):
		if isPalindrome((i+j)*(i-j)):
			maxPalindrome=(i+j)*(i-j)
		
	#Off-Centric Diagonal
	if (i)*(i-1)<maxPalindrome:
		print(maxPalindrome)
		break
	for j in range(0,maxMult-i+1):
		if isPalindrome((i+j)*(i-j-1)):
			maxPalindrome=(i+j)*(i-j-1)
            
