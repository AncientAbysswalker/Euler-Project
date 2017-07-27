# -*- coding: utf-8 -*-
"""
Created on Jul 26

@author: Abysswalker
"""

def strVal(string, baseVal=64):
	#Spaces are encoded to ASCII 0 so we do not consider them a problem here
	return sum(ord(i)-baseVal for i in string)

#Read left-to-right: Open document, read, remove "s, split on commas
nameList = open("names.txt","r").read().replace("\"","").split(",")
nameList.sort()

#sum over the multiplication of the string value of the sorted names by their indexes
print(sum(strVal(nameVal)*index for nameVal,index in zip(nameList,range(1,len(nameList)+1))))