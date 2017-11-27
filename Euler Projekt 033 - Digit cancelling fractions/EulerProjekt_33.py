# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 2017

@author: Ancient Abysswalker
"""

from math import gcd

denomprod = 1
numprod = 1
 
for c in range(1,10):
	for d in range(1,c):
		for n in range(1,d):
			if ((n*10 + c)*d == n*(c*10+d)):
				denomprod *= d
				numprod *= n
				
denomprod/=gcd(numprod,denomprod)
				
print(int(denomprod))