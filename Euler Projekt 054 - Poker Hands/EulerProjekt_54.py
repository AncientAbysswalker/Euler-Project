#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 18, 2018

@author: Abysswalker
"""

from collections import Counter
from os import path

def descendSort(inList):
	return sorted(list(inList))[::-1]

def pokerFile(pf,cardsinhand):
	filepath = path.join(path.dirname(__file__),pf)
		
	print("Checking existance of poker file")
	if not path.exists(filepath):
		raise ValueError("File does not exist, error...")
	else:
		print("File exists, parsing...")
		f=open(filepath, 'r')
		
		#Commit poker games to list
		games = f.read().splitlines()
		f.close()
				
		#Iterable for poker games
		gamiter=range(len(games))
		
		#Split each game into hands
		for i in gamiter:
			games[i]=games[i].split() #Split string into cardss in string form
			if len(games[i])%cardsinhand!=0:
				raise ValueError("This problem requires a file with 5-card hands on each line. One of the games does not fulfil this criterion...")
			
			#Convert card string to card class
			games[i][:]=[playingCard(x[0],x[1]) for x in games[i]]
			
		print("Successfully parsed!")
		
		#Split all cards into player hands
		return [[games[j][i:i + cardsinhand] for i in range(0, len(games[j]), cardsinhand)] for j in gamiter]

class playingCard:
	def __init__(self, value, suit):
		self.cardvalue = self.char2val(value)
		self.cardsuit = suit
		if suit not in ['S','C','D','H']:
			raise ValueError("Invalid Card Suit")
		
	def char2val(self, key):
		valDict = {'T': 10, 'J': 11,  'Q': 12, 'K': 13, 'A': 14}
		if key in valDict.keys():
			return valDict[key]
		elif int(key) in range(1,10):
			return int(key)
		raise ValueError("Invalid Card Value")
        
class hand:
	def __init__(self, rank, comparitive):
		self.rank = rank  
		self.comparitive = comparitive  
	
	def __gt__(self, other):
		return self.rank > other.rank or (self.rank == other.rank and self.comparitive > other.comparitive)
	
	def __lt__(self, other):
		return self.rank < other.rank or (self.rank == other.rank and self.comparitive < other.comparitive)
		
	def __eq__(self, other):
		return (self.rank == other.rank and self.comparitive == other.comparitive)
		
		
#Compare any number of hands
def compare_hands(competingHands):
     
	pH=[]
	
	for playerHand in competingHands:
		isFlush=False
		temp=[]
		suitlist=['S','C','D','H']
         
		map_value2quantity=Counter([card.cardvalue for card in playerHand]) #Dict of card values (key) with quantities
		map_quantity2values={1:[],2:[],3:[],4:[]} #Dict of quantities (key) with values
		for x,y in map_value2quantity.items():
			map_quantity2values[y].append(x)
		for i in range(1,5):
			map_quantity2values[i]=descendSort(map_quantity2values[i])
		
		map_suit2values={j:descendSort([card.cardvalue for card in playerHand if card.cardsuit == j]) for j in suitlist} #Dict of suits with associated cards in that suit
         
		if sum(1 for quantity in map_quantity2values.keys() if quantity > 4):
			raise ValueError("Someone cheated. There are more than five of a card face value")
		
		#If 5 or more of suit, we have a flush
		for facevalues in map_suit2values:
			if len(facevalues)>=5:
				isFlush=True
				temp.append(descendSort(facevalues)) #Append EACH ordered flush by suit, for checking straight and the high value card
		temp=descendSort(temp)

		#Check if straight (or royal) flush
		if temp:
			temp2=[]
			for flush in temp:
				for i in range(len(flush)-4):
					if flush[i] == flush[i+4]+4:
						temp2.append(flush[i:i+4])
						break #to next possible straight flush
			if temp2:
				pH.append(hand(9,sorted(temp2)[-1]))
				continue #to next player hand			
             
		#Check if we have a four of a kind
		if map_quantity2values[4]:
			pH.append(hand(8,(map_quantity2values[4]+map_quantity2values[3]+map_quantity2values[2]+map_quantity2values[1])[:2]))
			continue #to next player hand	
       
	   #Check if we have a full house
		if map_quantity2values[3] and map_quantity2values[2] or len(map_quantity2values[3])>1:
			pH.append(hand(7,(map_quantity2values[3]+map_quantity2values[2])[:2]))
			continue #to next player hand	

	   #Quick check if we had a flush before     
		if isFlush:
			pH.append(hand(6,temp[0]))
			continue #to next player hand	
		
		# #Check if we have a straight
		temp = descendSort(map_value2quantity.keys())
		temp2 = []
		for i in range(len(map_value2quantity.keys())-4):
			if temp[i] == temp[i+4]+4:
				temp2.append(temp[i:i+4])
				break #to post this as the highest for this player	
		if temp2:
			pH.append(hand(5,temp2))
			continue #to next player hand		
         
		#Check if we have a three of a kind
		if map_quantity2values[3]:
			pH.append(hand(4,(map_quantity2values[3]+map_quantity2values[1])[:3]))
			continue #to next player hand	
		
		#PSC - Check if we have two pair
		if len(map_quantity2values[2])>1:
			pH.append(hand(3,(map_quantity2values[2]+map_quantity2values[1])[:3]))
			continue #to next player hand	
       
	   #PSC - Check if we have a pair  
		if map_quantity2values[2]:
			pH.append(hand(2,(map_quantity2values[2]+map_quantity2values[1])[:4]))
			continue
		
		#PSC - Pass high card
		pH.append(hand(1,map_quantity2values[1][:5]))
	

	
	handList=[]
	playerList=[]
	for player,pHand in enumerate(pH):
		if not handList:
			handList=[pHand]
			playerList=[player]
		elif pHand > handList[0]:
			handList=[pHand]
			playerList=[player]
		elif pHand < handList[0]:
			continue
		else:
			handList.append(pHand)
			playerList.append(player)
	
	return playerList
     
#Parse file
gameset=pokerFile("p054_poker.txt",5)

counter=0
for each in gameset:
	temp=compare_hands(each)
	if len(temp)==1 and temp[0]==0:
		counter+=1
print(counter)
