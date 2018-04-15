# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12

@author: Abysswalker
"""

from itertools import permutations as permute

checkset=(2,3,5,7,11,13,17)
probsum=0

for p in permute("1234567890"):
	p=''.join(p)
	if all(int(p[i:i+3])%checkset[i-1] == 0 for i in range(1,8)):
		probsum+=int(p)
	
print(probsum)