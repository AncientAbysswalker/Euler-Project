# -*- coding: utf-8 -*-
"""
Created on Tue Jul  5 13:47:23 2017

@author: Ancient Abysswalker
"""

from Fibonacci import FibonacciNumber as Fibonacci
   
#First two fibonacci numbers
Fib=Fibonacci(2,1,2)
FibLim=int(4E6)
FibSum=0

#Sum to upper limit
while Fib.current<=FibLim:
    if Fib.eoc==2:
        FibSum+=Fib.current
    Fib=Fib.NextFib()

print(FibSum)