# Truncatable primes

## Problem Statement

The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

## Solution
This problem's premise is relatively simple; checking if a number is left or right trunkable is easily achieved through the use of a function. Initially I thought about this problem in a rather complicated manner, thinking to 'grow' these numbers from a seed. All trunkable primes like this could be grown recursively from a seed that is a prime, and must remain prime and trunkable continuously left or right all the way as it is grown. In theory this is viable, though I had issue getting it to produce reasonable results. Then I realized the simple solution - since I already have a file of primes up to the high 7-digits, I can just check the trunkable-ness of each prime in this set. Doing so took slightly longer than my original method likely would, but produced 11 primes as expected and the correct sum.