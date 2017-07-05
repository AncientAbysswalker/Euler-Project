# -*- coding: utf-8 -*-
"""
Created on Tue Jul  4 13:47:23 2017

@author: Ancient Abysswalker
"""

from math import floor

def seqsum(k):
    return int(k*(k + 1)/2)

#problem parameters
g=3
h=5
l=1000

#calculate sum limits
l-=1
alpha=floor(l/g)
beta=floor(l/h)
gamma=floor(l/(g*h))

#sum multiples of g and h
print(g*seqsum(alpha) + h*seqsum(beta) - g*h*seqsum(gamma))