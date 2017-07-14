# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11, 2017

@author: Abysswalker
"""

import requests
from bs4 import BeautifulSoup

r = requests.get('https://projecteuler.net/problem=8')
data = r.text
soup = BeautifulSoup(data, "lxml")

#Crawl Euler Page for number
probInt=int(''.join(soup.find_all('p')[1].text.split()))

#Produce list of digits
probList = [int(i) for i in str(probInt)]

#Calculate product
maxProd=0
numProd=13
for i in range(0,len(probList)-numProd+1):
	temp=1
	for j in range(i,i+numProd):
		temp*=probList[j]
	if temp>maxProd:
		maxProd=temp
		
print(maxProd)