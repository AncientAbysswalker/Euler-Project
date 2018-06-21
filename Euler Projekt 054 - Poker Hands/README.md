# Poker Hands

## Problem Statement



In the card game poker, a hand consists of five cards and are ranked, from lowest to highest, in the following way:

     High Card: Highest value card.
     One Pair: Two cards of the same value.
     Two Pairs: Two different pairs.
     Three of a Kind: Three cards of the same value.
     Straight: All cards are consecutive values.
     Flush: All cards of the same suit.
     Full House: Three of a kind and a pair.
     Four of a Kind: Four cards of the same value.
     Straight Flush: All cards are consecutive values of same suit.
     Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.

The cards are valued in the order:
2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.

If two players have the same ranked hands then the rank made up of the highest value wins; for example, a pair of eights beats a pair of fives. But if two ranks tie, for example, both players have a pair of queens, then highest cards in each hand are compared (see example 4 below); if the highest cards tie then the next highest cards are compared, and so on.

The file, poker.txt, contains one-thousand random hands dealt to two players. Each line of the file contains ten cards (separated by a single space): the first five are Player 1's cards and the last five are Player 2's cards. You can assume that all hands are valid (no invalid characters or repeated cards), each player's hand is in no specific order, and in each hand there is a clear winner.

How many hands does Player 1 win?

## Solution
My solution to this problem relies of three dicts that map the relationships between the suits, values, and quantities of cards in the hands. Using these three dictionaries, I determine how good the hand is and what the important cards for comparison are if a tie is reached. I initially wrote this to be extensible to larger hands (i.e. traditional poker where there are 5 shared cards and 2 private cards per player), though I have not fully added this functionality. The functions and comparisons should still work however. 

Through going through this problem and discussing it with a friend of mine, we took slightly different approaches though not by much. My code is significantly shorter, but also more difficult to read. This has brought my attention to Google's Python Style Guide and Test Driven Development. My coding methodology has always aired slightly on the side of a TDD-like system, but having read through the formal definitions for TDD and Google's Syle Guide have been invaluable, and I will be aiming to better my coding practices in the upcoming problems.