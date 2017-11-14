# Integer right triangles

## Problem Statement

If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?

## Solution
I did this solution with a reduced brute force method. The following is the problem criterion I was able to use:

<a href="https://www.codecogs.com/eqnedit.php?latex=p=a&plus;b&plus;c,\;&space;\;&space;c>a>b,\;&space;\;&space;c=\sqrt{a^2&plus;b^2}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?p=a&plus;b&plus;c,\;&space;\;&space;c>a>b,\;&space;\;&space;c=\sqrt{a^2&plus;b^2}" title="p=a+b+c,\; \; c>a>b,\; \; c=\sqrt{a^2+b^2}" /></a>

This is a definition true of all right-angle unit triangles, such as {3,4,5} and the ones stated in the problem. Side c is of course just the result of the pythagorean theorem. Since the perimeter must be less than 1000 no side can be more than 1000, meaning we can iterate over side a with lengths up to 1000, and side b up to the length of side a. If the pythagorean theorem results in an integer length side c, then we sum the sides and use the perimeter as the key in a dict where we store the number of ways we can make that perimeter. At the end, we simply pull the dict entry with the max value, and return the key since that represents the perimeter with max solutions.