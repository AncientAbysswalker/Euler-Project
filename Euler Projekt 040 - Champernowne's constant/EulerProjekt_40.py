# -*- coding: utf-8 -*-
"""
Created on Tue Nov 7 2017

@author: Ancient Abysswalker
"""

def digit_Champernowne(n):
	depth=0
	while n > 9*(10**depth)*(depth+1):
		n-=9*(10**depth)*(depth+1)
		depth+=1
	
	precedent=10**(depth)
	[fwd,digit]=divmod(n-1,depth+1)
	
	return int(str(precedent+fwd)[digit])

  
digit_sum=digit_Champernowne(1)*digit_Champernowne(10)*digit_Champernowne(100)*digit_Champernowne(1000)*digit_Champernowne(10000)*digit_Champernowne(100000)*digit_Champernowne(1000000)
print(digit_sum)