#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 18, 2018

@author: Abysswalker
"""

n_i=1
n_last=0
cnt=0

for _ in range(10**3):
    temp=2*n_i + n_last
    if len(str(n_i + temp)) > len(str(temp)):
        cnt+=1
    n_last, n_i = n_i, temp
print(cnt)