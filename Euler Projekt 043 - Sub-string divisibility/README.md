# Sub-string divisibility

## Problem Statement

The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order, but it also has a rather interesting sub-string divisibility property.

Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:

    d2d3d4=406 is divisible by 2
    d3d4d5=063 is divisible by 3
    d4d5d6=635 is divisible by 5
    d5d6d7=357 is divisible by 7
    d6d7d8=572 is divisible by 11
    d7d8d9=728 is divisible by 13
    d8d9d10=289 is divisible by 17

Find the sum of all 0 to 9 pandigital numbers with this property.

## Solution
It took me a little bit to understand exactly what this problem was asking me to do. Once I reallized what the problem wanted it was a relatively easy problem. Generating all the permutations of a set of numbers (in this case 0-9 pandigital) can be done simply with the python library itertools. It then becomes a simple task of checking if the 3-digit sub-strings are divisible by the ascending primes and summing the 0-9 pandigitals that pass the condition.