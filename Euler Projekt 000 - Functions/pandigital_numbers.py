# -*- coding: utf-8 -*-
"""
Created on Sat Mar 24 2018

@author: Ancient Abysswalker
"""

def isPandigital(number):
	check=len(str(number))
	if check>9:
		raise ValueError('A number cannot exceed 9 pandigital by definition')
	
	if set(str(number)) == set(str(i) for i in range(1,check+1)):
		return True
	return False	