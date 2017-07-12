# Special Pythagorean Triplet

## Problem Statement


A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
<a href="https://www.codecogs.com/eqnedit.php?latex=a^2&plus;b^2=c^2" target="_blank"><img src="https://latex.codecogs.com/gif.latex?a^2&plus;b^2=c^2" title="a^2+b^2=c^2" /></a>

For example, <a href="https://www.codecogs.com/eqnedit.php?latex=3^2&space;&plus;&space;4^2&space;=&space;9&space;&plus;&space;16&space;=&space;25&space;=&space;5^2" target="_blank"><img src="https://latex.codecogs.com/gif.latex?3^2&space;&plus;&space;4^2&space;=&space;9&space;&plus;&space;16&space;=&space;25&space;=&space;5^2" title="3^2 + 4^2 = 9 + 16 = 25 = 5^2" /></a>.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

## Solution
Relatively simple. The numbers a b and c can be written as follows:

<a href="https://www.codecogs.com/eqnedit.php?latex=a=n^2-m^2" target="_blank"><img src="https://latex.codecogs.com/gif.latex?a=n^2-m^2" title="a=n^2-m^2" /></a>

<a href="https://www.codecogs.com/eqnedit.php?latex=b=2nm" target="_blank"><img src="https://latex.codecogs.com/gif.latex?b=2nm" title="b=2nm" /></a>

<a href="https://www.codecogs.com/eqnedit.php?latex=c=n^2&plus;m^2" target="_blank"><img src="https://latex.codecogs.com/gif.latex?c=n^2&plus;m^2" title="c=n^2+m^2" /></a>

<a href="https://www.codecogs.com/eqnedit.php?latex=n>m" target="_blank"><img src="https://latex.codecogs.com/gif.latex?n>m" title="n>m" /></a>

This means that we can simplify the sum of the three to

<a href="https://www.codecogs.com/eqnedit.php?latex=a&plus;b&plus;c=2n^2&plus;2nm" target="_blank"><img src="https://latex.codecogs.com/gif.latex?a&plus;b&plus;c=2n^2&plus;2nm" title="a+b+c=2n^2+2nm" /></a>

I simply wrote a script to crawl this range to find the single pair of numbers that could produce 1000. The only clever thing is that I crawled in reverse with regards to m (down from n-1 to 1) and broke to the next iteration if the expression was less than 1000. This simply saved computation iterations.