# -*- coding: utf-8 -*-
"""
Created on Wed Jul  5 10:01:09 2017

@author: Ancient Abysswalker
"""

class FibonacciNumber:
    """Fibonacci Number Class
    Contains:
        current - the current fibonacci number
        last    - the last fibonacci number
        eoc     - counter 0,1,2 to indicate if the number is even. Number is even if the counter is 2
    """

    def __init__(self, current, last, eoc):
        self.current = current
        self.last = last
        self.eoc = eoc
        
    def NextFib(self):
        """Next Fibonacci Number"""
        return FibonacciNumber(self.current+self.last,self.current,(self.eoc+1)%3)