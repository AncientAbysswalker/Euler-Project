# Amicable numbers

## Problem Statement

Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n). If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.


## Solution
I produced two solutions for this problem - one is better in time complexity and one is better in saving memory space.

To save on time complexity, my original proposed solution, I decided to make a boolean array of all numbers in the intended range (i.e. the number is the index keying to whether that number has been tried yet) and just adding to a sum when a number is amicable

To *possibly* save on space, I decided to create a list of amicable numbers as they were generated, and to check if new numbers are amicable and not in that list - to not double-count pairs.

I think inarguably the first solution is superior, especially considering the boolean array can be smaller than the amicable number array, depending on the counts, and considering list search is O(n) and list access is O(1).