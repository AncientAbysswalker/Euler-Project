# Largest palindrome product

## Problem Statement
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.

## Solution
I saw this problem as essentially a matrix of the multiples of the numbers. This merely became a matrix traversal problem after that. I have included a 20x20 multiplication table below for ease of understanding on my method here. I the multiplication table the largest numbers exist in the lower right. The matrix is fully symmetric and thus only half of the entries must be considered. By traversing the matrix up the diagonal, we get the square multiples, and traversing the perpendicular diagonal all the entries decrease. I chose to move along the red line shown and then up the perpendicular centric (blue) and non-centric (green) perpendicular diagonals to find the palindromic numbers, once one has been found I store it as the current max and continue looking for another. If the value found on the red line is ever less than the current max we stop the traversal because no other entries on my traversal path can ever be larger than the max currently stored.

<a href="https://github.com/AncientAbysswalker/Projekt-Euler/blob/master/Euler Projekt 4/20x20.gif" target="_blank"><img src="https://github.com/AncientAbysswalker/Projekt-Euler/blob/master/Euler Projekt 4/20x20.gif" title="Multiplication Table" /></a>
