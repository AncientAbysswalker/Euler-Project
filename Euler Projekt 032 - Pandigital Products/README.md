# Pandigital Products

## Problem Statement

We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.

## Solution
The first thing I did is write a simple function to check if a number is 1-9 pandigital. I wrote a function that is not strictly correct, as it is too generous, but as we are not considering anything with a length greater than 9 it works anyways with one fewer check and thus some memory saved. I simply check that the number provided has 9 individual numbers for digits except 0, which obviously fails if I provide it 1234567899, but as I said we avoid this case.

This problem requires the numbers in the multiplication problem to be pandigital, and for this to occur, there must be exactly 9 digits among the three numbers. To solve this problem there are two cases, one is that we multiply a one digit number by a four digit number to get a four digit number. The other is that we multiply a two digit number by a three digit number to get a four digit number. I test each product to see if it is pandigital, and if so I add the product to a set. Since a set cannot include duplicate entries this solves the HINT in the problem statement. At the end I simply sum over the set for the answer.