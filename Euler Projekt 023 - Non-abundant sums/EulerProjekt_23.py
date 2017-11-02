# -*- coding: utf-8 -*-
"""
Created on Fri Oct 6

@author: Abysswalker
"""

from os import path

#Sum proper denominators
def spd(number):
	spd=0
	for i in range(1,int(number/2)+1):
		if number%i == 0:
			spd+=i
	return spd

#Generate an abundant number set
def abunSet(maxAbun):
	filepath = path.join(path.dirname(__file__),"abunSet.txt")
	abunnum=set()
	
	print("Checking existance of generated abundant number file")
	if not path.exists(filepath):
		print("File does not exist, generating...")

		for checknum in range(12,maxAbun):
			if spd(checknum)>checknum:
				abunnum.add(checknum)
				
		abunFile = open(filepath,"w")
		abunFile.write(str(abunnum)[1:-1])
		print("File generated. Next run of this program should skip this step!")
	else:
		print("File exists, parsing...")
		abunFile=open(filepath, 'r')
		for num in abunFile.read().split(','):
			abunnum.add(int(num))
		print("Parsing complete!")
	
	abunFile.close()
	return abunnum

abunNumSet=abunSet(28123)
abunSumSet=set(i+j for i in abunNumSet for j in abunNumSet if j<=28123-i)
fullSet=set(range(1,28123+1))
print("Sum =", sum(fullSet-abunSumSet))