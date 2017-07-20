# -*- coding: utf-8 -*-
"""
Created on Jul 19, 2017

@author: Abysswalker
"""

import requests
from bs4 import BeautifulSoup

r = requests.get('https://projecteuler.net/problem=13')
data = r.text
soup = BeautifulSoup(data, "lxml")

#Crawl Euler Page for number and sort to array
intList = [int(i) for i in soup.find_all('div')[10].text.strip().splitlines()]

#Sum the numbers
numSum=sum(i for i in intList)
print("Full Number:",numSum)
print("First 10:",str(numSum)[0:10])