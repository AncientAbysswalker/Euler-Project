# Even Fibonacci numbers

## Problem Statement
Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

## Solution
This problem is relatively straight-forward. Fibonacci sequence numbers follow a consistent pattern, with every third number being even after the first two numbers 1 and 2. This means that <a href="https://www.codecogs.com/eqnedit.php?latex=\mathcal{F}_{i&plus;1}&space;=&space;\mathcal{F}_{i}&plus;\mathcal{F}_{i-1}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\mathcal{F}_{i&plus;1}&space;=&space;\mathcal{F}_{i}&plus;\mathcal{F}_{i-1}" title="\mathcal{F}_{i+1} = \mathcal{F}_{i}+\mathcal{F}_{i-1}" /></a> with the even elements corresponding to <a href="https://www.codecogs.com/eqnedit.php?latex=\mathcal{F}_{1&plus;3n},&space;n\epsilon&space;\mathbb{Z}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\mathcal{F}_{1&plus;3n},&space;n\epsilon&space;\mathbb{Z}" title="\mathcal{F}_{1+3n}, n\epsilon \mathbb{Z}" /></a> if the numbers 1 and 2 are elements 0 and 1 respective.

I simply made a fibonacci class object that stores the current value in the sequence, past value in the sequence, and a counter for determining if it is even or odd.
