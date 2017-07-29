# Lexicographic permutations

## Problem Statement

A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

     012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

## Solution
I started this problem with writing down permutations so I could try to identify a pattern. With something this ordered I know there had to be a discernable pattern. I started by mapping digit shifts, and while this may be a viable way to generate lexicographic permutations the patterns are complex and hard to identify. 

This did however lead me to reallizing the easy solution. If we have all the permutations in order and we want to identify when a given digit k will change, this is dependant on how many digits are after it - let's say n. For example, the lowest permutation in this problem is 0123456789 - when 5 will change? there are 4 digits after 5 (6,7,8,9), and it just so happens there are exactly 24 or 4! permutations before the 5 changes. The next question is what does this change to? Looking at the generated permutations the 5 changes to the lowest number larger than it on the list - in this case 6. In general the numbers will remain the lowest they can without repeating a permutation - so the 25th permutaion (24+1) will be 0123465789

Basically in the end this all comes together to say that if we want the millionth permutation (999999+1), we take 999999 mod 9! - this tells us that there are 2 9!s that can fit into 999999. Subtract 2*9! from 999999 and mod this against 8! (and continue all the way down to 0!). These multiples of the factorials are actually the indices of a list containing the possible digits. Pictures say a thousand words, so just look below at the graphic I made showwing this mapping. 