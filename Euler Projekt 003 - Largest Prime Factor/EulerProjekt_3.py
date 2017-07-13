# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6

@author: Ancient Abysswalker
"""
   
def checkPrime(number,Primes):
    for Prime in Primes:
        if number%Prime == 0:
            return False
    return True

#Problem definition
N=600851475143
P=[2]
F=[]

#Sum to upper limit
Factorized=False
while not Factorized:
    [tempQuotient,tempRemainder]=(divmod(N,P[-1]))
    if tempRemainder==0:
        F.append(P[-1])
        N=tempQuotient
    else:
        tmpC=P[-1]
        while True:
            tmpC+=1
            if checkPrime(tmpC,P):
                P.append(tmpC)
                break
            else:
                if N/tmpC<P[-1]:
                    if N!=1: F.append(N)
                    Factorized=True
                    break
print("Prime Factors are:" + str(F))
