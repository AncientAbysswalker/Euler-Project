# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11, 2017

@author: Abysswalker
"""

#Problem Definition
isSum=False
intendedSum=1000

#Cycle until sum is reached
n=2
m=0
while not isSum:
    for tempM in reversed(range(1,n)):
        if n*(n+tempM)<intendedSum/2:
            n+=1
            break
        elif n*(n+tempM)==intendedSum/2:
            isSum=True
            m=tempM
            break

print("a=" + str(n*n-m*m))
print("b=" + str(2*n*m))
print("c=" + str(n*n+m*m))
print("Product=" + str((n*n-m*m)*(n*n+m*m)*(2*m*n)))