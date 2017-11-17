# -*- coding: utf-8 -*-
"""
Created on Sat Nov 11 2017

@author: Ancient Abysswalker
"""

from math import sqrt

def triNum(number):
	return int(number*(number+1)/2)

def isTriNum(number):
	test=(-1+sqrt(1+8*number))/2
	return test==int(test)

#####

def pentNum(number):
	return int(number*(3*number-1)/2)

def isPentNum(number):
	test=(1+sqrt(1+24*number))/6
	return test==int(test)

#####

def hexNum(number):
	return int(number*(2*number-1))

def isHexNum(number):
	test=(1+sqrt(1+8*number))/4
	return test==int(test)

#####

def figNum(number,x):
	return int(number*((x-2)*number+(4-x))/2)

def isFigNum(number,x):
	test=((x-4)+sqrt((4-x)**2+8*(x-2)*number))/(2*(x-2))
	return test==int(test)
	
	
	
	
	
	