# -*- coding: utf-8 -*-
"""
Created on Sat Nov 11 2017

@author: Ancient Abysswalker
"""

from figurate_numbers import *

n=1 #Index of hex numbers to start at
select=2 #Which match of tri=hex=pent do we want to look for?

s=0
while s<select:
	n+=1
	if isTriNum(hexNum(n)) and isPentNum(hexNum(n)):
		s+=1
	
print(HexNum(n))