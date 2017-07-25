# -*- coding: utf-8 -*-
"""
Created on Fri Jul 21, 2017

@author: Abysswalker
"""

a=['','one','two','three','four','five','six','seven','eight','nine']
b=['ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
c=['','','twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']
d=['',' thousand',' million',' billion',' trillion',' quadrillion',' quintillion']

def n2t_3digit(num3d):
	if num3d>999:
		raise ValueError('More than 3 digits passed to 3-digit function')
	if num3d!=int(num3d):
		raise ValueError('Non-integer was passed')
	
	retstr=''
	[hundreds,num2d]=divmod(num3d,100)

	#Hundreds digit
	if hundreds!=0:
		retstr+= a[hundreds] + ' hundred'
		if num2d!=0:
			retstr+= ' and '
				 
	#Determine in teens or not
	if num2d>=10 and num2d<=19:
		retstr+=b[num2d-10]
	else:
		[tens,ones]=divmod(num2d,10)
		retstr+=c[tens]
		if tens!=0 and ones!=0:
			retstr+='-'
		retstr+=a[ones]
		
	return retstr

def n2t(num, thouplace=0):
	if thouplace>len(d)-1:
		raise ValueError('Exceeded definition of named 10^3 multiples')
	
	[nextTxt,parse]=divmod(num,1000)
	
	if nextTxt==0:
		return n2t_3digit(parse) + d[thouplace]
	return n2t(nextTxt,thouplace+1) + ' ' +  n2t_3digit(parse) + d[thouplace]