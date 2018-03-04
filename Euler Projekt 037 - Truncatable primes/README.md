# Circular primes

## Problem Statement

The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime. There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?

## Solution
This is a relatively easy problem. I wrote a function to rotate any input text, in this case the set of promes we are testing below one million. I modified my previous code regarding prime generation to allow me to store the primes as a file for future re-runs, and to also store the values as a set, which is a more efficient data structure than a list for determining if an object is an element of a set.

For each of the primes below one million, I check the rotations to see if they are also included in the set; if all rotations were included in the set I added them to a new set of circular primes. I also removed the circular primes from the original primes list so that I wouldn't print out circular sets more than once, but I want to point out that this slows down the code as it is extra unnecessary steps for the processor. As it is, the set data structure is extremely efficient at determining whether an object is an element of a set and removing elements takes more time than is saved in the checking process for the extra elements in question.