# -*- coding: utf-8 -*-
"""
Created on Sun Aug 6 2017

@author: Abysswalker
"""
		
import requests
from bs4 import BeautifulSoup

r = requests.get('https://projecteuler.net/problem=18')
data = r.text
soup = BeautifulSoup(data, "lxml")

#Crawl Euler Page for number and sort to array
triPath=[[int(j) for j in i] for i in [row.split() for row in soup.find_all('p')[4].text.strip().splitlines()]]

for i in reversed(range(len(triPath)-1)):
	for j in range(i+1):
		triPath[i][j]=max(triPath[i][j]+triPath[i+1][j],triPath[i][j]+triPath[i+1][j+1])

print(triPath[0][0])