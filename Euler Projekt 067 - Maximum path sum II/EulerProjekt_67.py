# -*- coding: utf-8 -*-
"""
Created on Sun Aug 6 2017

@author: Abysswalker
"""
		
#Crawl text document
triPath = [[int(j) for j in i] for i in [row.split() for row in open("tri.txt","r").read().splitlines()]]

for i in reversed(range(len(triPath)-1)):
	for j in range(i+1):
		triPath[i][j]=max(triPath[i][j]+triPath[i+1][j],triPath[i][j]+triPath[i+1][j+1])

print(triPath[0][0])