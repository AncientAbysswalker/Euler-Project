# -*- coding: utf-8 -*-
"""
Created on Jul 26

@author: Abysswalker
"""

size=1001

#Sum over quadratics
print(1 + sum(16*n**2-28*n+16 for n in range(2,int(size/2)+2)))