# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 2017

@author: Abysswalker
"""

from math import factorial

def isFactSum(number):
	return number==sum([factorial(j) for j in [int(i) for i in str(number)]])
		

mysum=0
for checks in range(10,2540160+1):
	if isFactSum(checks):
		mysum+=checks
		
print(mysum)