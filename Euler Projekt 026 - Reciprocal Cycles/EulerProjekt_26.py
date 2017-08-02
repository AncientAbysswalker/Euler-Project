# -*- coding: utf-8 -*-
"""
Created on Jul 29

@author: Abysswalker
"""

def red25(number):
	for reducers in [2,5]:
		while number>1:
			if number%reducers==0:
				number/=reducers
			else:
				break
	return int(number)

d=0
l=0
for i in range(2,1000):
	a=red25(i)
	if a!=1:
		j=1
		while True:
			if (10**j)%a==1:
				break
			else:
				j+=1
		
		if j>l:
			l=j
			d=i
			
print("length", l, "for denom",d)