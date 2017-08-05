# -*- coding: utf-8 -*-
"""
Created on Aug 5

@author: Abysswalker
"""

powlis=[]
for i in range(2,101):
	for j in range(2,101):
		if i**j not in powlis:
			powlis.append(i**j)
			
print(len(powlis))