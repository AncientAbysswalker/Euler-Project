#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 18, 2018

@author: Abysswalker
"""

def isPalindrome(num):
    num=str(num)
    if num == num[::-1]:
        return True
    return False

def isLychel(num):
    if isPalindrome(num):
        return False
    for _ in range(50):
        num+=int(str(num)[::-1])
        if isPalindrome(num):
            return False
    return True

upperLim=10**4
cnt=0

for i in range(1,upperLim):
    if isLychel(i):
        cnt+=1
print(cnt)