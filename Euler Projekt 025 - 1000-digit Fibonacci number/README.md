# 1000-digit Fibonacci number

## Problem Statement

The Fibonacci sequence is defined by the recurrence relation:

     Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.

Hence the first 12 terms will be:

     F1 = 1
     F2 = 1
     F3 = 2
     F4 = 3
     F5 = 5
     F6 = 8
     F7 = 13
     F8 = 21
     F9 = 34
     F10 = 55
     F11 = 89
     F12 = 144

The 12th term, F12, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

## Solution
This problem is easily solvable without the need for any programming at all. Binet's Formula is a formula for the n-th Fibonacci number, and is given by

<a href="https://www.codecogs.com/eqnedit.php?latex=Fib(n)&space;=&space;\frac{\varphi^n-(-\varphi)^{-n})&space;}{\sqrt{5}}=\frac{\varphi^n}{\sqrt{5}}-\frac{(-1)^n}{\varphi^n\sqrt{5}}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?Fib(n)&space;=&space;\frac{\varphi^n-(-\varphi)^{-n})&space;}{\sqrt{5}}=\frac{\varphi^n}{\sqrt{5}}-\frac{(-1)^n}{\varphi^n\sqrt{5}}" title="Fib(n) = \frac{\varphi^n-(-\varphi)^{-n}) }{\sqrt{5}}=\frac{\varphi^n}{\sqrt{5}}-\frac{(-1)^n}{\varphi^n\sqrt{5}}" /></a>

Where φ is the golden ratio 1.6180339887....

10^999 is the first number to have 1000 digits, so we want the first Fibonacci number that fulfills this condition

<a href="https://www.codecogs.com/eqnedit.php?latex=Fib(n)&space;=&space;\frac{\varphi^n}{\sqrt{5}}-\frac{(-1)^n}{\varphi^n\sqrt{5}}&space;>&space;10^{999}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?Fib(n)&space;=&space;\frac{\varphi^n}{\sqrt{5}}-\frac{(-1)^n}{\varphi^n\sqrt{5}}&space;>&space;10^{999}" title="Fib(n) = \frac{\varphi^n}{\sqrt{5}}-\frac{(-1)^n}{\varphi^n\sqrt{5}} > 10^{999}" /></a>

We also observe that if n is sufficiently large that the second term vanishes entirely, which is not unreasonable since they vanish fast (I tested the 150th Fibonacci and my calculator said the second term is 0 - and I know the answer is much larger than the 150th Fibonacci number)

<a href="https://www.codecogs.com/eqnedit.php?latex=\frac{\varphi^n}{\sqrt{5}}-\frac{(-1)^n}{\varphi^n\sqrt{5}}&space;>&space;10^{999}\rightarrow&space;\frac{\varphi^n}{\sqrt{5}}>&space;10^{999}\;&space;for\;&space;n\;&space;sufficiently\;&space;large" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\frac{\varphi^n}{\sqrt{5}}-\frac{(-1)^n}{\varphi^n\sqrt{5}}&space;>&space;10^{999}\rightarrow&space;\frac{\varphi^n}{\sqrt{5}}>&space;10^{999}\;&space;for\;&space;n\;&space;sufficiently\;&space;large" title="\frac{\varphi^n}{\sqrt{5}}-\frac{(-1)^n}{\varphi^n\sqrt{5}} > 10^{999}\rightarrow \frac{\varphi^n}{\sqrt{5}}> 10^{999}\; for\; n\; sufficiently\; large" /></a>

So this becomes

<a href="https://www.codecogs.com/eqnedit.php?latex=\varphi^n>&space;10^{999}\sqrt{5}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\varphi^n>&space;10^{999}\sqrt{5}" title="\varphi^n> 10^{999}\sqrt{5}" /></a>

Log both sides

<a href="https://www.codecogs.com/eqnedit.php?latex=log(\varphi^n)>&space;log(10^{999}\sqrt{5})" target="_blank"><img src="https://latex.codecogs.com/gif.latex?log(\varphi^n)>&space;log(10^{999}\sqrt{5})" title="log(\varphi^n)> log(10^{999}\sqrt{5})" /></a>

<a href="https://www.codecogs.com/eqnedit.php?latex=n\cdot&space;log(\varphi)>&space;999&plus;log(\sqrt{5})\rightarrow&space;n&space;>&space;\frac{999&plus;log(\sqrt{5})}{log(\varphi)}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?n\cdot&space;log(\varphi)>&space;999&plus;log(\sqrt{5})\rightarrow&space;n&space;>&space;\frac{999&plus;log(\sqrt{5})}{log(\varphi)}" title="n\cdot log(\varphi)> 999+log(\sqrt{5})\rightarrow n > \frac{999+log(\sqrt{5})}{log(\varphi)}" /></a>

So we want the first fibonacci number where n is greater than or equal to the identity on the right. The easiest way to do this is to round up the number produced:

<a href="https://www.codecogs.com/eqnedit.php?latex=n&space;=ciel\left&space;(&space;\frac{999&plus;log(\sqrt{5})}{log(\varphi)}&space;\right&space;)=4782" target="_blank"><img src="https://latex.codecogs.com/gif.latex?n&space;=ciel\left&space;(&space;\frac{999&plus;log(\sqrt{5})}{log(\varphi)}&space;\right&space;)=4782" title="n =ciel\left ( \frac{999+log(\sqrt{5})}{log(\varphi)} \right )=4782" /></a>