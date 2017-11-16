# Coded triangle numbers

## Problem Statement

The n<sup>th</sup> term of the sequence of triangle numbers is given by, t<sub>n</sub> = ½n(n+1); so the first ten triangle numbers are:

     1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t<sub>10</sub>. If the word value is a triangle number then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common English words, how many are triangle words?

## Solution
This problem was not particularly difficult, as I was able to recycle most of my code from [Euler Projekt - Name Scores 22](https://github.com/AncientAbysswalker/Projekt-Euler/tree/master/Euler%20Projekt%20022%20-%20Names%20scores). I use the same method of extracting words from the file and the same method of assigning values to the words. The only thing to do was to determine if a word is triangular. Since the formula to produce a triangle number is a simple quadratic, the inverse process simplifies to an application of the quadratic formula. While it is true that this gives two solutions, one will always be negative, and thus we only need to consider one root in checking if the number is triangular.

<a href="https://www.codecogs.com/eqnedit.php?latex=t_n(n)=\frac{1}{2}n(n&plus;1)\rightarrow&space;0=n^2&plus;n-2\cdot&space;t_n(n)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?t_n(n)=\frac{1}{2}n(n&plus;1)\rightarrow&space;0=n^2&plus;n-2\cdot&space;t_n(n)" title="t_n(n)=\frac{1}{2}n(n+1)\rightarrow 0=n^2+n-2\cdot t_n(n)" /></a>

<a href="https://www.codecogs.com/eqnedit.php?latex=n=\frac{-1\pm&space;\sqrt{1&plus;8\cdot&space;t_n(n)}}{2}\rightarrow&space;n=\frac{-1&space;&plus;&space;\sqrt{1&plus;8\cdot&space;t_n(n)}}{2}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?n=\frac{-1\pm&space;\sqrt{1&plus;8\cdot&space;t_n(n)}}{2}\rightarrow&space;n=\frac{-1&space;&plus;&space;\sqrt{1&plus;8\cdot&space;t_n(n)}}{2}" title="n=\frac{-1\pm \sqrt{1+8\cdot t_n(n)}}{2}\rightarrow n=\frac{-1 + \sqrt{1+8\cdot t_n(n)}}{2}" /></a>