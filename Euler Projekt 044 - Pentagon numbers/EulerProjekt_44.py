# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 2017

@author: Ancient Abysswalker
"""

from math import sqrt

def sumdivcheck(k,j):
	if k==j:
		return False
	sump=(1+sqrt(1+12*(3*(k**2+j**2)-(k+j))))/6
	divp=(1+sqrt(1+12*(3*(k**2-j**2)+(j-k))))/6
	return sump==int(sump) and divp==int(divp)

def loops():
	k=1
	while True:
		for j in range(1,k):
			if sumdivcheck(k,j):
				return [int((3*(k**2-j**2)+(j-k))/2),k,j]
		k+=1
			
[d,k,j]=loops()
print(d,"k="+str(k),"j="+str(j))
		