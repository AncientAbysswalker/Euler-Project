# Distinct prime factors

## Problem Statement

The first two consecutive numbers to have two distinct prime factors are:

    14 = 2 × 7
    15 = 3 × 5

The first three consecutive numbers to have three distinct prime factors are:

    644 = 2² × 7 × 23
    645 = 3 × 5 × 43
    646 = 2 × 17 × 19.

Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?


## Solution
This solution was relatively simple. I did not see a mathematical shortcut for this problem, so I opted for a brute-force method. Starting from the lowest multiple of n distinct primes, we iterate upwards and count sequential occurrences of numbers that have n distinct prime factors.