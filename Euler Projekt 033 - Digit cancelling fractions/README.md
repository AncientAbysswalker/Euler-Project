# Digit cancelling fractions

## Problem Statement

The fraction <sup>49</sup>/<sub>98</sub> is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that <sup>49</sup>/<sub>98</sub> = <sup>4</sup>/<sub>8</sub>, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, <sup>30</sup>/<sub>50</sub> = <sup>3</sup>/<sub>5</sub>, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the denominator.

## Solution
I was a bit confused as to the specifics of 'trivial examples' as first, but I quickly reallized that this means any fractions including 0s. Let us say c is the common digit between the numerator and denominator to cancel, and n and d are the other digits in the numerator and denominator respectively. Given this, and the fact that we are dealing with proper fractions (i.e. The fraction is less than 1).

<a href="https://www.codecogs.com/eqnedit.php?latex=1\leq&space;n&space;<&space;d&space;\leq&space;9;\;&space;n,d\epsilon&space;\mathbb{N}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?1\leq&space;n&space;<&space;d&space;\leq&space;9;\;&space;n,d\epsilon&space;\mathbb{N}" title="1\leq n < d \leq 9;\; n,d\epsilon \mathbb{N}" /></a>

<a href="https://www.codecogs.com/eqnedit.php?latex=1\leq&space;c&space;\leq&space;9;\;&space;c\epsilon&space;\mathbb{N}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?1\leq&space;c&space;\leq&space;9;\;&space;c\epsilon&space;\mathbb{N}" title="1\leq c \leq 9;\; c\epsilon \mathbb{N}" /></a>

Given this, we can have one of four separate canceling scenarios:

<a href="https://www.codecogs.com/eqnedit.php?latex=1)\;&space;\frac{10c&plus;n}{10c&plus;d}=\frac{n}{d}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?1)\;&space;\frac{10c&plus;n}{10c&plus;d}=\frac{n}{d}" title="1)\; \frac{10c+n}{10c+d}=\frac{n}{d}" /></a>

<a href="https://www.codecogs.com/eqnedit.php?latex=2)\;&space;\frac{10n&plus;c}{10c&plus;d}=\frac{n}{d}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?2)\;&space;\frac{10n&plus;c}{10c&plus;d}=\frac{n}{d}" title="2)\; \frac{10n+c}{10c+d}=\frac{n}{d}" /></a>

<a href="https://www.codecogs.com/eqnedit.php?latex=3)\;&space;\frac{10c&plus;n}{10d&plus;c}=\frac{n}{d}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?3)\;&space;\frac{10c&plus;n}{10d&plus;c}=\frac{n}{d}" title="3)\; \frac{10c+n}{10d+c}=\frac{n}{d}" /></a>

<a href="https://www.codecogs.com/eqnedit.php?latex=4)\;&space;\frac{10n&plus;c}{10d&plus;c}=\frac{n}{d}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?4)\;&space;\frac{10n&plus;c}{10d&plus;c}=\frac{n}{d}" title="4)\; \frac{10n+c}{10d+c}=\frac{n}{d}" /></a>

Let us expand on these equations, one by one:

<a href="https://www.codecogs.com/eqnedit.php?latex=1)\;&space;\frac{10c&plus;n}{10c&plus;d}=\frac{n}{d}\rightarrow&space;10cd&plus;nd=10cn&plus;nd\rightarrow&space;n=d" target="_blank"><img src="https://latex.codecogs.com/gif.latex?1)\;&space;\frac{10c&plus;n}{10c&plus;d}=\frac{n}{d}\rightarrow&space;10cd&plus;nd=10cn&plus;nd\rightarrow&space;n=d" title="1)\; \frac{10c+n}{10c+d}=\frac{n}{d}\rightarrow 10cd+nd=10cn+nd\rightarrow n=d" /></a>

This fails because we must have n<d by our previous definitions.

<a href="https://www.codecogs.com/eqnedit.php?latex=2)\;&space;\frac{10n&plus;c}{10c&plus;d}=\frac{n}{d}\rightarrow&space;10nd&plus;cd=10cn&plus;nd\rightarrow&space;9nd=10cn-cd\rightarrow&space;9n(d-i)=i(n-d)\;&space;\therefore&space;n<d<i" target="_blank"><img src="https://latex.codecogs.com/gif.latex?2)\;&space;\frac{10n&plus;c}{10c&plus;d}=\frac{n}{d}\rightarrow&space;10nd&plus;cd=10cn&plus;nd\rightarrow&space;9nd=10cn-cd\rightarrow&space;9n(d-i)=i(n-d)\;&space;\therefore&space;n<d<i" title="2)\; \frac{10n+c}{10c+d}=\frac{n}{d}\rightarrow 10nd+cd=10cn+nd\rightarrow 9nd=10cn-cd\rightarrow 9n(d-i)=i(n-d)\; \therefore n<d<i" /></a>

<a href="https://www.codecogs.com/eqnedit.php?latex=3)\;&space;\frac{10c&plus;n}{10d&plus;c}=\frac{n}{d}\rightarrow&space;10cd&plus;nd=10nd&plus;cn\rightarrow&space;9nd=10cd-cn\rightarrow&space;9n(n-i)=i(d-n)\;&space;\therefore&space;i<n<d" target="_blank"><img src="https://latex.codecogs.com/gif.latex?3)\;&space;\frac{10c&plus;n}{10d&plus;c}=\frac{n}{d}\rightarrow&space;10cd&plus;nd=10nd&plus;cn\rightarrow&space;9nd=10cd-cn\rightarrow&space;9n(n-i)=i(d-n)\;&space;\therefore&space;i<n<d" title="3)\; \frac{10c+n}{10d+c}=\frac{n}{d}\rightarrow 10cd+nd=10nd+cn\rightarrow 9nd=10cd-cn\rightarrow 9n(n-i)=i(d-n)\; \therefore i<n<d" /></a>

Further expanding on the above, we get

<a href="https://www.codecogs.com/eqnedit.php?latex=3)\;&space;n-c=\frac{c}{9}-\frac{cn}{9d}=\frac{c}{9}\left&space;(1-\frac{n}{d}&space;\right&space;)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?3)\;&space;n-c=\frac{c}{9}-\frac{cn}{9d}=\frac{c}{9}\left&space;(1-\frac{n}{d}&space;\right&space;)" title="3)\; n-c=\frac{c}{9}-\frac{cn}{9d}=\frac{c}{9}\left (1-\frac{n}{d} \right )" /></a>

Looking at this however, the left side is larger than one, while the right must be less than one - so scenario 3 holds no solution.

<a href="https://www.codecogs.com/eqnedit.php?latex=4)\;&space;\frac{10n&plus;c}{10d&plus;c}=\frac{n}{d}\rightarrow&space;10nd&plus;cd=10nd&plus;cn\rightarrow&space;n=d" target="_blank"><img src="https://latex.codecogs.com/gif.latex?4)\;&space;\frac{10n&plus;c}{10d&plus;c}=\frac{n}{d}\rightarrow&space;10nd&plus;cd=10nd&plus;cn\rightarrow&space;n=d" title="4)\; \frac{10n+c}{10d+c}=\frac{n}{d}\rightarrow 10nd+cd=10nd+cn\rightarrow n=d" /></a>

This fails because we must have n<d by our previous definitions.

Now that we have all of the scenarios considered, all that we have to do is carry out the code to check scenario 2. If we increment over the ranges for c,d,n given in scenario and check if they fulfill the criterion, then we simply multiply the numerator and denominator numbers. Then lastly find the greatest common denominator and reduce the denominator for that to discorver the answer.
