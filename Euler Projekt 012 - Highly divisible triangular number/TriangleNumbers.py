# -*- coding: utf-8 -*-
"""
Created on Jul 19 2017

@author: Ancient Abysswalker
"""

class TriangleNumber:
	"""Triangle Number Class
	Contains:
		value   - the value of the triangle number term
		term    - the term number
	"""

	def __init__(self, value=1, term=1):
		self.value = value
		self.term = term
        
	def NextTri(self):
		"""Next Triangle Number"""
		return TriangleNumber(self.value+self.term+1,self.term+1)