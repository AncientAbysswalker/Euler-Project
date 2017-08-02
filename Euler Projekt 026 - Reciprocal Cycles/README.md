# Reciprocal cycles

## Problem Statement



A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

     1/2	= 	0.5
     1/3	= 	0.(3)
     1/4	= 	0.25
     1/5	= 	0.2
     1/6	= 	0.1(6)
     1/7	= 	0.(142857)
     1/8	= 	0.125
     1/9	= 	0.(1)
     1/10	= 	0.1 

Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

## Solution
First off, I know that for any divisor that is a pure multiple of 2s and 5s the decimal is non-repeating. All other fractions have repeats. I learned this back in school, though it isn't common knowledge from my understanding. The next part of the problem then becomes determining how long the repeating sequence is by producing each decimal - though to me this is too brute-force. The number of decimals is actually related to the denominator.

<a href="https://www.codecogs.com/eqnedit.php?latex=given\;&space;\frac{1}{d},\;&space;\left&space;\{&space;length\;&space;repeat&space;\right&space;\}=b\;&space;for\;&space;(10^b)\%d=1" target="_blank"><img src="https://latex.codecogs.com/gif.latex?given\;&space;\frac{1}{d},\;&space;\left&space;\{&space;length\;&space;repeat&space;\right&space;\}=b\;&space;for\;&space;(10^b)\%d=1" title="given\; \frac{1}{d},\; \left \{ length\; repeat \right \}=b\; for\; (10^b)\%d=1" /></a>

This allows for much faster solving of the problem.