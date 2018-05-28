# Square root convergents

## Problem Statement

It is possible to show that the square root of two can be expressed as an infinite continued fraction.

     √ 2 = 1 + 1/(2 + 1/(2 + 1/(2 + ... ))) = 1.414213...

By expanding this for the first four iterations, we get:

     1 + 1/2 = 3/2 = 1.5
     1 + 1/(2 + 1/2) = 7/5 = 1.4
     1 + 1/(2 + 1/(2 + 1/2)) = 17/12 = 1.41666...
     1 + 1/(2 + 1/(2 + 1/(2 + 1/2))) = 41/29 = 1.41379...

The next three expansions are 99/70, 239/169, and 577/408, but the eighth expansion, 1393/985, is the first example where the number of digits in the numerator exceeds the number of digits in the denominator.

In the first one-thousand expansions, how many fractions contain a numerator with more digits than denominator?

## Solution
To me, recursive problems like this always scream 'pattern' loudly to my brain. The first thing I did for this problem was immediately pull out a notepad to start sketching the terms in this series. The result became quickly apparent; the following definition became obvious:

<a href="https://www.codecogs.com/eqnedit.php?latex=E_i=\frac{n_{i&plus;1}&plus;n_i}{n_{i&plus;1}};\;\;&space;n_{i&plus;1}=2&space;\cdot&space;n_i&plus;n_{i-1};\;\;i\epsilon&space;N_0" target="_blank"><img src="https://latex.codecogs.com/gif.latex?E_i=\frac{n_{i&plus;1}&plus;n_i}{n_{i&plus;1}};\;\;&space;n_{i&plus;1}=2&space;\cdot&space;n_i&plus;n_{i-1};\;\;i\epsilon&space;N_0" title="E_i=\frac{n_{i+1}+n_i}{n_{i+1}};\;\; n_{i+1}=2 \cdot n_i+n_{i-1};\;\;i\epsilon N_0" /></a>

<a href="https://www.codecogs.com/eqnedit.php?latex=n_0=0;\;\;n_1=1" target="_blank"><img src="https://latex.codecogs.com/gif.latex?n_0=0;\;\;n_1=1" title="n_0=0;\;\;n_1=1" /></a>

Where E<sub>i</sub> is the i<sup>th</sup> expansion of the series. Given this, I simply iterated over the series to i=1000 and checked which have the number of digits in the numerator greater than the denominator.