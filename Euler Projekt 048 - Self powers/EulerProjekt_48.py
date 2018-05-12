# -*- coding: utf-8 -*-
"""
Created on Sat May 12

@author: Abysswalker
"""

#Vars
uLim=10**3 #Upper limit of self-power
sumP=0 #sum of self powers
numDigits=10

#This conmvoluted for generates a set of odd composites by removing primes and evens
for i in range(1,uLim+1):
	temp=i
	for _ in range(i-1):
		temp*=i
		temp=int(str(temp)[-numDigits:]) #Truncate to 10 digits
	sumP+=temp
	sumP=int(str(sumP)[-numDigits:]) #Truncate to 10 digits
	
print(sumP)