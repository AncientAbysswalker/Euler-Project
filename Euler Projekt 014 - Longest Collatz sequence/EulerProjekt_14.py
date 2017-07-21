# -*- coding: utf-8 -*-
"""
Created on Jul 20, 2017
@author: Ancient Abysswalker
"""

def collatz(n):
	if n==1:
		return 1
	if n%2==0:
		return 1 + collatz(n/2)
	return 1 + collatz(3*n+1)

#problem parameters
probMax=1000000

#calculate longest collatz sequence
maxLen=0
maxNum=0

for i in range(2,probMax):
	tempLen=collatz(i)
	if tempLen>maxLen:
		maxLen=tempLen
		maxNum=i
		
print(maxNum)