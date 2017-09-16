# Digit fifth powers

## Problem Statement

Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

     1634 = 1^4 + 6^4 + 3^4 + 4^4
     8208 = 8^4 + 2^4 + 0^4 + 8^4
     9474 = 9^4 + 4^4 + 7^4 + 4^4

As 1 = 1^4 is not a sum it is not included. The sum of these numbers is 1634 + 8208 + 9474 = 19316. Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

## Solution
The first thing to do here is determine the range through which we need to search. The maximum sum of the fifth-power digits is 9^5 multiplied by the number of digits in the number. From the problem's definition we can determine that we do not need to go any farther than 6 digits as this is where the value 999999 surpasses 6*9^5=354294 (with five digits we get 99999 < 5*9^5=295245). This is because at 6 digits, the number can no longer be written as a sum of it's digits as it is too large!

Funny enough I typo'd the original code and you only need to run to 5 digits because there are apparently no numbers in the range of 99999 to 999999 that can be written as their sum of fifth-power digits. Interresting :)

`      9 < 59049`
     99 < 118098
    999 < 177147
   9999 < 236196
  99999 < 295245
 999999 > 354294
9999999 > 413343
