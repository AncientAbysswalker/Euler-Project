# Multiples of 3 and 5

## Problem Statement
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23. Find the sum of all the multiples of 3 or 5 below 1000.

## Solution
I see this problem as more of a mathematical problem than a programming one. Consider the sum of multiples of 3 and 5 to be two sets, who are of course not mutually exclusive. Since the sets overlap, if we sum each individual set, we will have overlap. The answer to the question is the sum of the union of the two sets. If we consider the sum of all multiples (or the problem's answer) to be S, and the two sets to be A and B, then we can break the union as follows

<a href="https://www.codecogs.com/eqnedit.php?latex=S=\sum&space;A\cup&space;B=\sum&space;A&plus;\sum&space;B-\sum&space;A\cap&space;B" target="_blank"><img src="https://latex.codecogs.com/gif.latex?S=\sum&space;A\cup&space;B=\sum&space;A&plus;\sum&space;B-\sum&space;A\cap&space;B" title="S=\sum A\cup B=\sum A+\sum B-\sum A\cap B" /></a>

Now, the sums we are considering are the multiples of 3 and 5 for multiples existing below 1000. So that means the elements of set A are multiples of 3, the elements of B are multiples of 5, and the lements of the union are multiples of both - i.e. 15

<a href="https://www.codecogs.com/eqnedit.php?latex=S=\sum_{k=1}^{\alpha}&space;3k&plus;\sum_{k=1}^{\beta}&space;5k-\sum_{k=1}^{\gamma}&space;15k" target="_blank"><img src="https://latex.codecogs.com/gif.latex?S=\sum_{k=1}^{\alpha}&space;3k&plus;\sum_{k=1}^{\beta}&space;5k-\sum_{k=1}^{\gamma}&space;15k" title="S=\sum_{k=1}^{\alpha} 3k+\sum_{k=1}^{\beta} 5k-\sum_{k=1}^{\gamma} 15k" /></a>

This just leaves the upper limits. If we consider the sums to all be of the form below, then we can also logicall follow the limit is also as below

<a href="https://www.codecogs.com/eqnedit.php?latex=S=\sum_{k=1}^{\epsilon&space;}&space;jk&space;\;&space;and\:&space;jk<1000&space;\rightarrow&space;\epsilon&space;<\frac{1000}{j}&space;\rightarrow&space;\epsilon&space;=floor(\frac{999}{j})" target="_blank"><img src="https://latex.codecogs.com/gif.latex?S=\sum_{k=1}^{\epsilon&space;}&space;jk&space;\;&space;and\:&space;jk<1000&space;\rightarrow&space;\epsilon&space;<\frac{1000}{j}&space;\rightarrow&space;\epsilon&space;=floor(\frac{999}{j})" title="S=\sum_{k=1}^{\epsilon } jk \; and\: jk<1000 \rightarrow \epsilon <\frac{1000}{j} \rightarrow \epsilon =floor(\frac{999}{j})" /></a>

Using this logic, the python script becomes a few lines long and spits out the correct answer with ease.