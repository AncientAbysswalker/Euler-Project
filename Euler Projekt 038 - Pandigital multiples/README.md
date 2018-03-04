# Pandigital multiples

## Problem Statement

Take the number 192 and multiply it by each of 1, 2, and 3:

     192 × 1 = 192
     192 × 2 = 384
     192 × 3 = 576

By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?

## Solution
This problem is fairly simple to solve using an iterative loop. Let us call the first number k, and the second number n (as defined). The number of digits in k dictates how high n can get - as we need a total of 9 digits in all the combined numbers.

     For two digit numbers n can get up to 4 (with the hope that the four numbers will have digit counts of 2,2,2,3).
	 For three digit numbers n can get up to 3 (with the hope that all the numbers will have 3 digits).
	 For four digit numbers n can get up to 2 (with the hope that the first number will have 4 digits, and the second will have 5).

I ran under the assumption that k cannot be one digit. I could not determine a formal proof of this, so I ran it anyways without any simplifications.