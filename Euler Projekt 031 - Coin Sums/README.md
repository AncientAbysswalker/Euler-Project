# Coin Sums

## Problem Statement

In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:

     1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).

It is possible to make £2 in the following way:

     1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p

How many different ways can £2 be made using any number of coins?

## Solution
This problem is easiest solved using a dynamic program that recurs over coin sums. I did this by making a bag of all possible coins to sum with, and a function to add the coins. The function is called with an inital sum of 0. The function then is instructed to try adding each coin from the bag to see what the sum is. If the sum is less than our target value, the function calls a child copy of its process to continue adding more coins. If the sum is equivalent to our target, we add one to the count of how many ways to sum to the target. If the sum is larger than our target, the process dies and nothing is added to the count.

I understand this process is not the easiest to visualize, I had some problems visualizing it at first too, so I made the gif below to demonstrate this for a lower value coin like 5 pence.

<a href="https://github.com/AncientAbysswalker/Projekt-Euler/blob/master/Euler%20Projekt%20031%20-%20Coin%20Sums/CoinGIF.gif"><img src="https://github.com/AncientAbysswalker/Projekt-Euler/blob/master/Euler%20Projekt%20031%20-%20Coin%20Sums/CoinGIF.gif" title="Coin Sums" /></a>
