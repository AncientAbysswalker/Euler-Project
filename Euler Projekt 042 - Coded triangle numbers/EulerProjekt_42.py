# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 2017

@author: Ancient Abysswalker
"""

from math import sqrt

def triWord(number):
	test=(-1+sqrt(1+8*strVal(number)))/2
	return test==int(test)

def strVal(string, baseVal=64):
	#Spaces are encoded to ASCII 0 so we do not consider them a problem here
	return sum(ord(i)-baseVal for i in string)

#Read left-to-right: Open document, read, remove "s, split on commas
wordList = open("words.txt","r").read().replace("\"","").split(",")
wordList.sort()

#count the number of triangular words
print(sum(triWord(word) for word in wordList))