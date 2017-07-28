# -*- coding: utf-8 -*-
"""
Created on Jul 27

@author: Abysswalker
"""

#Sum proper denominators
def spd(number):
	spd=0
	for i in range(1,int(number/2)+1):
		if number%i == 0:
			spd+=i
	return spd

#Problem Variable
maxNum=10000


#Find and sume the amicables
amicNum=[]
for a in range(2,maxNum):
	b=spd(a)
	if b<maxNum and spd(b)==a:
		if b not in amicNum and a!=b:
			amicNum.append(a)
			amicNum.append(b)
			
print(sum(i for i in amicNum))