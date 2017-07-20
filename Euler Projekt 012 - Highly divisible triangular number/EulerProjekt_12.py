# -*- coding: utf-8 -*-
"""
Created on Jul 19, 2017

@author: Abysswalker
"""

from math import sqrt
from TriangleNumbers import TriangleNumber

#Problem Variables
factMin=500

#Problem Solving
curNum=TriangleNumber()
factors=0
while factors <= factMin:
	curNum=curNum.NextTri()
	factors=0
	for i in range(1,int(sqrt(curNum.value))):
		if curNum.value%i == 0:
			factors+=2

print("Value:", curNum.value)
print("Term:", curNum.term)