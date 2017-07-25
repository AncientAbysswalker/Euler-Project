# -*- coding: utf-8 -*-
"""
Created on Sat Jul 22 17:36:07 2017

@author: Laurence
"""

def genFebDays(year):
	if year%4 == 0:
		if year%100 == 0 and not year%400 == 0:
			return 28
		return 29			
	return 28
	
def genDateDays(year,day,string=False):
	dayList=[31,genFebDays(year),31,30,31,30,31,31,30,31,30,31]
	dayStr=['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']

	sucList=[day]
	for i in range(0,12):
		sucList.append((day+sum(dayList[0:i+1]))%7)

	if string==True:
		return [dayStr[i] for i in sucList[:-1]],dayStr[sucList[-1]]
	return sucList[:-1],sucList[-1]
		
sumSun=0
mont=2
for years in range(1901,2001):
	monStrt,mont=genDateDays(years,mont)
	print(monStrt)
	for monStrt2 in monStrt:
		if monStrt2==0:
			sumSun+=1

print(sumSun)