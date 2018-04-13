# Pandigital prime

## Problem Statement

We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?

## Solution
This problem's premise is relatively simple. Since I already have a file consisting of all primes to a relatively high number, I simply run through all primes in the list and check if the prime is pandigital and larger than the last recorded pandigital prime. This provides the answer, assuming that the prime in question is not higher than the largest one in my list (hooray large primes), which is the case here.