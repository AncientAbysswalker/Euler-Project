# -*- coding: utf-8 -*-
"""
Created on Tue Jul 12, 2017

@author: Abysswalker
"""

import requests
from bs4 import BeautifulSoup

r = requests.get('https://projecteuler.net/problem=11')
data = r.text
soup = BeautifulSoup(data, "lxml")

#Crawl Euler Page for number and sort to array
intArr = [[int(j) for j in i] for i in [row.split() for row in soup.find_all('p')[1].text.strip().splitlines()]]
#print(intArr)
lenArr=len(intArr)
maxProd=0

#Vertical
for cols in range(0,lenArr):
	for rows in range(0,lenArr-3):
		temp=intArr[rows][cols]*intArr[rows+1][cols]*intArr[rows+2][cols]*intArr[rows+3][cols]
		if temp>maxProd:
			maxProd=temp
			
#Horizontal
for cols in range(0,lenArr-3):
	for rows in range(0,lenArr):
		temp=intArr[rows][cols]*intArr[rows][cols+1]*intArr[rows][cols+2]*intArr[rows][cols+3]
		if temp>maxProd:
			maxProd=temp
			
#\\\\\\\\\\\\\\\\\\\\\
for cols in range(0,lenArr-3):
	for rows in range(0,lenArr-3):
		temp=intArr[rows][cols]*intArr[rows+1][cols+1]*intArr[rows+2][cols+2]*intArr[rows+3][cols+3]
		if temp>maxProd:
			maxProd=temp

#/////////////////////
for cols in range(3,lenArr):
	for rows in range(0,lenArr-3):
		temp=intArr[rows][cols]*intArr[rows+1][cols-1]*intArr[rows+2][cols-2]*intArr[rows+3][cols-3]
		if temp>maxProd:
			maxProd=temp

print(maxProd)