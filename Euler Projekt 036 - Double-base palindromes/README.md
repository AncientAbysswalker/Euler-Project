# Double-base palindromes

## Problem Statement

The decimal number, 585 = 1001001001(binary), is palindromic in both bases. Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.
(Please note that the palindromic number, in either base, may not include leading zeros.)

## Solution
My solution for this problem utilizes my code from Projekt 4 for checking if a number is a palindrome. This problem wants us to check the numbers for if both their decimal and binary representations are palindromes. The computer actually stores data values in binary, but PRINTS the value as decimal for us humans because, at least in most modern societies, we have adopted the convention of base 10 mathematics. Since the function I wrote before takes the printed representation and checks for palindrome, we need to get the printed representation of binary. Python allows this with the bin() function and will print the value with a suffix - i.e. bin(585)=0b1001001001. Cut off the first two characters of that string and we nicely have the representation we need.