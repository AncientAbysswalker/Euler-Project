# Self powers

## Problem Statement

The series, 1<sup>1</sup> + 2<sup>2</sup> + 3<sup>3</sup> + ... + 10<sup>10</sup> = 10405071317.

Find the last ten digits of the series, 1<sup>1</sup> + 2<sup>2</sup> + 3<sup>3</sup> + ... + 1000<sup>1000</sup>.

## Solution
Let us call the function that observes only the last x digits of n T(n,x). From this, the following property is observable:

<a href="https://www.codecogs.com/eqnedit.php?latex=\mathcal{T}(n^{4},x)&space;=&space;\mathcal{T}(\mathcal{T}(\mathcal{T}(n&space;\cdot&space;n,x)&space;\cdot&space;n,x)&space;\cdot&space;n,x)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\mathcal{T}(n^{4},x)&space;=&space;\mathcal{T}(\mathcal{T}(\mathcal{T}(n&space;\cdot&space;n,x)&space;\cdot&space;n,x)&space;\cdot&space;n,x)" title="\mathcal{T}(n^{4},x) = \mathcal{T}(\mathcal{T}(\mathcal{T}(n \cdot n,x) \cdot n,x) \cdot n,x)" /></a>

<a href="https://www.codecogs.com/eqnedit.php?latex=e.g.\;&space;\;&space;\mathcal{T}(987^{4},5)&space;=&space;\mathcal{T}(\mathcal{T}(\mathcal{T}(987&space;\cdot&space;987,5)&space;\cdot&space;987,5)&space;\cdot&space;987,5)&space;=&space;40561" target="_blank"><img src="https://latex.codecogs.com/gif.latex?e.g.\;&space;\;&space;\mathcal{T}(987^{4},5)&space;=&space;\mathcal{T}(\mathcal{T}(\mathcal{T}(987&space;\cdot&space;987,5)&space;\cdot&space;987,5)&space;\cdot&space;987,5)&space;=&space;40561" title="e.g.\; \; \mathcal{T}(987^{4},5) = \mathcal{T}(\mathcal{T}(\mathcal{T}(987 \cdot 987,5) \cdot 987,5) \cdot 987,5) = 40561" /></a>

Doing this allows one to recursively multiply and then truncate the number down to what we need. In python this is not entirely necessary, since memory is dynamically allocated and I can't overflow the integers - but doing this is essential for other languages such as C, so I did it for posterity's sake.
