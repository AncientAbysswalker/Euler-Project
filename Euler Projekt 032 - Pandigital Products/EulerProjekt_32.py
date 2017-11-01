# -*- coding: utf-8 -*-
"""
Created on Fri Oct 6

@author: Abysswalker
"""

def isPandigital9(number):
	temp=set(str(number))
	if len(temp) == 9 and ("0" not in temp):
		return True
	return False

products=set()

#Scenario 1 Sets
s1set1=set(range(1,9+1))
s1set2=set(range(1000,9999+1))

#Scenario 2 Sets
s2set1=set(range(10,99+1))
s2set2=set(range(100,999+1))

for i in s1set1:
	for j in s1set2:
		if isPandigital9(str(i)+str(j)+str(i*j)) and len(str(i*j))==4:
			products.add(i*j)

for i in s2set1:
	for j in s2set2:
		if isPandigital9(str(i)+str(j)+str(i*j)) and len(str(i*j))==4:
			products.add(i*j)

print(sum(products))
