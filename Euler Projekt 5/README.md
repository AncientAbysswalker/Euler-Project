# Smallest multiple

## Problem Statement
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

## Solution
Probably the easiest conceptually so far. The number 2520 is the smallest product of primes - but not in the sense that you can multiply the primes directly. The formula for the minimum multiple we are looking for is <a href="https://www.codecogs.com/eqnedit.php?latex=\prod_{i}^{&space;}&space;p_{i}^{n_{i}}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\prod_{i}^{&space;}&space;p_{i}^{n_{i}}" title="\prod_{i}^{ } p_{i}^{n_{i}}" /></a> where <a href="https://www.codecogs.com/eqnedit.php?latex=p_{i}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?p_{i}" title="p_{i}" /></a> is the indexed prime and <a href="https://www.codecogs.com/eqnedit.php?latex=n_{i}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?n_{i}" title="n_{i}" /></a> is the maximum count of that prime as a factor in a given number in the range desired (in our case 1 through 20).

For example, in the range 1 through 10, we have primes 2 3 5 7. With regards to the non-primes 4 6 8 9 10 we get:
4 = 2 x 2

6 = 2 x 3

8 = 2 x 2 x 2

9 = 3 x 3

10 = 2 x 5

So we can say that the maximum counts of the primes are 3 2 5 and 0 for 2 3 5 and 7 respectively, so the product becomes <a href="https://www.codecogs.com/eqnedit.php?latex=2^3\cdot&space;3^2\cdot&space;5^1\cdot&space;7^0&space;=&space;2520" target="_blank"><img src="https://latex.codecogs.com/gif.latex?2^3\cdot&space;3^2\cdot&space;5^1\cdot&space;7^0&space;=&space;2520" title="2^3\cdot 3^2\cdot 5^1\cdot 7^0 = 2520" /></a>

The only other thing of note here is I decided to play around with dicts for this problem's solution
