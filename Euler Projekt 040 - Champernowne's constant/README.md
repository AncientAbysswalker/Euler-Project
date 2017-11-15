# Champernowne's constant

## Problem Statement

An irrational decimal fraction is created by concatenating the positive integers:

     0.123456789101112131415161718192021...

It can be seen that the 12<sup>th</sup> digit of the fractional part is 1.

If d<sub>n</sub> represents the n<sup>th</sup> digit of the fractional part, find the value of the following expression.

d<sub>1</sub> × d<sub>10</sub> × d<sub>100</sub> × d<sub>1000</sub> × d<sub>10000</sub> × d<sub>100000</sub> × d<sub>1000000</sub>

## Solution
My logic in this problem is very pattern-based. Instead of brute forcing the solution, I reallized that the Champernowne constant has a very deterministic pattern. While I'm sure this pattern can be easily looked up online, I decided to reproduce it myself.

The first thing I see is that we can split the constant up into ranges, determined by the size of the concatenated integers. Given an inclusive range, say a through b, the numbger of entries is (b-a)+1. For 1 through 9, this gives 9. For 10 through 99, this gives 90. For 100 through 999, this gives 900, and so on. This tells us how many numbers are in the range, but not the number of digits; this is given by multiplying the previous numbers by their integers' size respectively. Cool, that means one-digit numbers make up the digits 1-9 of Champernowne, two digits make up 10-189, three make up 190-2889.

In order to determine what digit range we are situated in, simply given a number n for the overall digit, I dynamically step through the ranges by subtracting the number of digits in the last range. For example, if I wanted the 12th digit that would mean I want the 3th digit of the 10-99 range of concatenated integers.

The next half of the battle is determining how far in the intended range we need to search. Using division with the number of digits to traverse and the integer sizes we can find this. Using our example, if we have n=3 in the two-digit range of integers that means 3/2 results in 1 with a remainder of 1. The quotient, q, is how far we are from the starting number in the group - in this case 10+q=11, which means the 13th digit comes from the number 11. The remainder refers to which digit in the previously mentioned number we want, starting from 0 - in this case our number is 11 and the remainder is 1, so we want the second digit, which is 1.

I understand this process is somewhat confusing, and I admit myself that this took a bit of tinkering and thought to get it to function properly, but it works beautifully. I made the following infographic to help visualize this.

<a href="https://github.com/AncientAbysswalker/Projekt-Euler/tree/master/Euler%20Projekt%20040%20-%20Champernowne's%20constant/champernowne.png" target="_blank"><img src="https://github.com/AncientAbysswalker/Projekt-Euler/tree/master/Euler%20Projekt%20040%20-%20Champernowne's%20constant/champernowne.png" title="champernowne" /></a>