# -*- coding: utf-8 -*-
"""
Created on Jul 20, 2017
@author: Ancient Abysswalker
"""

from math import factorial as fact

def binom(n,k):
	if n == k:
		return 1
	if k > n:
		return 0
	return int(fact(n)/fact(k)/fact(n-k))

#lattice grid is 1 larger than grid size
latGrid=21

#print the number of paths
pathCnt=binom(2*(latGrid-1),latGrid-1)
print(pathCnt)