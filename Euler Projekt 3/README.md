# 	Largest prime factor

## Problem Statement
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143?

## Solution
This problem is essentially just finding the factors of a natural number. Every natural number is either a prime number itself or a product of multiple prime numbers. My logic here is relatively simple - I try to divide the given number by each sequential prime until the remainder is no longer 0. What I mean by this is if I divide a numer by a prime, if the remainder is 0 it is divisible by that prime, if it is not 0 then we can try the next, higher prime.

Now the fun thing here is that I figured out (hadn't really thought about this before) that if you divide a number by a prime and the result is less than the previous prime (the prime before the one we are currently trying) then the number is a prime number. This simply reduces the number of calculations that I have to do before I know that the remainder is prime itself, as opposed to dividing 600851475143 by every prime in the range 2 through 600851475143.
