# -*- coding: utf-8 -*-
"""
Created on Tue Jul  10

@author: Ancient Abysswalker
"""

#Problem definition, upperLimit must be >=2
upperLimit=100
sum=0

#Find sum square difference
for i in range(1,upperLimit):
	sum+=int(2*i*(upperLimit*(upperLimit-i) - (upperLimit-i-1)*(upperLimit-i)/2))
	
print(sum)
	