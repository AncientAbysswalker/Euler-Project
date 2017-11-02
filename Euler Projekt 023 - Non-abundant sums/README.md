# Non-abundant sums

## Problem Statement

A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

## Solution

The way I think of this problem is in sets. We only really care about numbers in the range of 1 to 28123, as all numbers beyond this are by default the sum of two abundant numbers. I will call this set A. Next, we want a set of abundant numbers. I wrote a special function to store the results of abundant number generration, since it takes a bit to generate them; I generated them up to the aforementioned limit of 28123. Generating a set of all possible sums of numbers from this set gives us the list of all numbers within our range that can be generated as the sum of two abundant numbers - call this set B. This leaves us simply with set C, where C=A-B, is the set of all numbers which cannot be written as the sum of two abundant numbers. Summing over this set is our answer.