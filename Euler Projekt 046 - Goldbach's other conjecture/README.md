# Goldbach's other conjecture

## Problem Statement

It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.

     9 = 7 + 2×12
     15 = 7 + 2×22
     21 = 3 + 2×32
     25 = 7 + 2×32
     27 = 19 + 2×22
     33 = 31 + 2×12

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?

## Solution
I took a fairly straight forward approach to this problem. First I generate a set of odd composite numbers; to do this I generate a set of all the counting numbers and remove primes and even numbers. I then begin going through these numbers and applying Goldbach's conjecture to see if it fails. For each odd composite I start with checking the larger primes (less than the composite) and working my way down. For each composite C and attempted prime P, we get that the squared number must follow the equality below:

<a href="https://www.codecogs.com/eqnedit.php?latex=2i^2&plus;P=C\rightarrow&space;\sqrt{\frac{C-P}{2}}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?2i^2&plus;P=C\rightarrow&space;\sqrt{\frac{C-P}{2}}" title="2i^2+P=C\rightarrow \sqrt{\frac{C-P}{2}}" /></a>

So if i is an integer value, then we have passed Goldbach's conjecture. If we work our way through all the primes and still haven't met this condition then we have found the number that fails Goldbach's conjecture.