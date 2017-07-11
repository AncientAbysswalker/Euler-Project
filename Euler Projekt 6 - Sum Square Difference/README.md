# Sum Square Difference

## Problem Statement
The sum of the squares of the first ten natural numbers is,
1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)^2 = 552 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640. Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

## Solution
This essentially comes down to simplifying the expression. This relationship is just two sums:
<a href="https://www.codecogs.com/eqnedit.php?latex={\left(\sum_{i=1}^{n}&space;i&space;\right)}^{2}-&space;\sum_{i=1}^{n}&space;i^2" target="_blank"><img src="https://latex.codecogs.com/gif.latex?{\left(\sum_{i=1}^{n}&space;i&space;\right)}^{2}-&space;\sum_{i=1}^{n}&space;i^2" title="{\left(\sum_{i=1}^{n} i \right)}^{2}- \sum_{i=1}^{n} i^2" /></a>

And the first sum is special and can be simplified as follows:
<a href="https://www.codecogs.com/eqnedit.php?latex={\left(\sum_{i=1}^{n}&space;i&space;\right)}^{2}-&space;\sum_{i=1}^{n}&space;i^2&space;=&space;\left(&space;\sum_{i=1}^{n}&space;i^2&space;&plus;&space;2&space;\sum_{j=2}^{n}&space;\sum_{i<j}^{&space;}&space;i\cdot&space;j\right)-&space;\sum_{i=1}^{n}&space;i^2&space;\rightarrow&space;2&space;\sum_{j=2}^{n}&space;\sum_{i<j}^{&space;}&space;i\cdot&space;j\right)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?{\left(\sum_{i=1}^{n}&space;i&space;\right)}^{2}-&space;\sum_{i=1}^{n}&space;i^2&space;=&space;\left(&space;\sum_{i=1}^{n}&space;i^2&space;&plus;&space;2&space;\sum_{j=2}^{n}&space;\sum_{i<j}^{&space;}&space;i\cdot&space;j\right)-&space;\sum_{i=1}^{n}&space;i^2&space;\rightarrow&space;2&space;\sum_{j=2}^{n}&space;\sum_{i<j}^{&space;}&space;i\cdot&space;j\right)" title="{\left(\sum_{i=1}^{n} i \right)}^{2}- \sum_{i=1}^{n} i^2 = \left( \sum_{i=1}^{n} i^2 + 2 \sum_{j=2}^{n} \sum_{i<j}^{ } i\cdot j\right)- \sum_{i=1}^{n} i^2 \rightarrow 2 \sum_{j=2}^{n} \sum_{i<j}^{ } i\cdot j\right)" /></a>

This last step I had to do by hand and pattern recognition

1     x (2 + 3 + 4 + ... + (n-3) + (n-2) + (n-1) + n)

2     x (    3 + 4 + ... + (n-3) + (n-2) + (n-1) + n)

3     x (        4 + ... + (n-3) + (n-2) + (n-1) + n)

...

(n-4) x (			 ... + (n-3) + (n-2) + (n-1) + n)

(n-3) x (                          (n-2) + (n-1) + n)

(n-2) x (                                  (n-1) + n)

(n-1) x (                                          n)

Observing this pattern, I saw that if we write each factor as <a href="https://www.codecogs.com/eqnedit.php?latex=\sum&space;a_i,\;&space;\;&space;a_i=x(y\cdot&space;n&plus;z)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\sum&space;a_i,\;&space;\;&space;a_i=x(y\cdot&space;n&plus;z)" title="\sum a_i,\; \; a_i=x(y\cdot n+z)" /></a> then I get <a href="https://www.codecogs.com/eqnedit.php?latex=a_i=i\left&space;(&space;n\cdot(n-i)-\frac{(n-i-1)(n-i)}{2}&space;\right&space;)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?a_i=i\left&space;(&space;n\cdot(n-i)-\frac{(n-i-1)(n-i)}{2}&space;\right&space;)" title="a_i=i\left ( n\cdot(n-i)-\frac{(n-i-1)(n-i)}{2} \right )" /></a>

So my code is simply responsible for calculating the simple sum

<a href="https://www.codecogs.com/eqnedit.php?latex=Sum=2\cdot&space;\sum_{i=1}^{n-1}&space;i\left&space;(&space;n\cdot(n-i)-\frac{(n-i-1)(n-i)}{2}&space;\right&space;)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?Sum=2\cdot&space;\sum_{i=1}^{n-1}&space;i\left&space;(&space;n\cdot(n-i)-\frac{(n-i-1)(n-i)}{2}&space;\right&space;)" title="Sum=2\cdot \sum_{i=1}^{n-1} i\left ( n\cdot(n-i)-\frac{(n-i-1)(n-i)}{2} \right )" /></a>