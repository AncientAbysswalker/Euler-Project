# Digit factorials

## Problem Statement

145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.

## Solution
Simple problem. First I determined where the sum of the factorial of the digits of a number can no longer equal that number. This occurs at 2540160, which is every digit being 9 in a 7 digit number. (7*9!) 8 digit numbers cannot be written as a sume of their digits. 

After this it was simply a matter of writing a function to check if the sum of the primes of the digits is the number, and added to a cumulative sum if it is.