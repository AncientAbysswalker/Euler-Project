# -*- coding: utf-8 -*-
"""
Created on Tue Nov 7

@author: Abysswalker
"""

from math import sqrt

perims={}

for i in range(2,1000):
	for j in range(2,i):
		p=sqrt(i**2+j**2)+i+j
		
		if p<=1000 and p.is_integer():
			perims[int(p)]=perims.get(p, 0)+1
		
print(max(perims.keys(), key=(lambda key: perims[key])))