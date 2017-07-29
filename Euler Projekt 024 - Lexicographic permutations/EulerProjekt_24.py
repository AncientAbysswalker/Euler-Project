# -*- coding: utf-8 -*-
"""
Created on Jul 27

@author: Abysswalker
"""

from math import factorial

upperRng=9      #Digits 0-9 inclusive
lexSet=1000000  #The nth lex permutation
lm=True        #Print list map?

#Generate list of digits 0-9 inclusive
digits=list(range(0,upperRng+1))

lex=0           #Lex Number
lexSet-=1       #Because we technically need 1 less than the nth number from the initial permutation
for i in reversed(range(0,upperRng+1)):
	a=int(lexSet/factorial(i))  #How many times i! fits in lexSet
	if lm: print(a)             #list map
	lex+=digits[a]*10**i        #Map correct digit
	lexSet-=factorial(i)*a      #Reduce lexSet to ignore i!*a
	digits.pop(a)               #Remove digit from pool
	
print(lex)