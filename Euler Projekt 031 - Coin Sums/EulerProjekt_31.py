# -*- coding: utf-8 -*-
"""
Created on Jul 20, 2017
@author: Ancient Abysswalker
"""

def recurCoin(N,S,val):
	sumr=0
	for coin in S:
		if coin >= val:
			if coin < N:
				sumr+=recurCoin(N-coin,S,coin)
			if coin == N:
				sumr+=1	
		
	return sumr
	
	

#problem parameters
S=[1,2,5,10,20,50,100,200,400]

#Print the recursion
print(recurCoin(200,S,0))