# -*- coding: utf-8 -*-
"""
Created on Aug 30

@author: Abysswalker
"""

list5=[]

for i in range(2,4*9**6):
	if i == sum([int(j)**5 for j in str(i)]):
		list5.append(i)
		
print(sum(list5))