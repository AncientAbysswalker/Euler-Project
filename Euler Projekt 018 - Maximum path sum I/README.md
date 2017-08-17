# Maximum path sum I

## Problem Statement

By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

<a href="https://github.com/AncientAbysswalker/Projekt-Euler/blob/master/Euler%20Projekt%20018%20-%20Maximum%20path%20sum%20I/SmallTri.png" target="_blank"><img src="https://github.com/AncientAbysswalker/Projekt-Euler/blob/master/Euler%20Projekt%20018%20-%20Maximum%20path%20sum%20I/SmallTri.png" title="Triangle" /></a>
	 
That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:

<a href="https://github.com/AncientAbysswalker/Projekt-Euler/blob/master/Euler%20Projekt%20018%20-%20Maximum%20path%20sum%20I/LargeTri.png" target="_blank"><img src="https://github.com/AncientAbysswalker/Projekt-Euler/blob/master/Euler%20Projekt%20018%20-%20Maximum%20path%20sum%20I/LargeTri.png" title="Triangle" /></a>

NOTE: As there are only 16384 routes, it is possible to solve this problem by trying every route. However, Problem 67, is the same challenge with a triangle containing one-hundred rows; it cannot be solved by brute force, and requires a clever method! ;o)

## Solution
I spent some time considering this problem. If we were to calculate every possible combination for this triangle (the brute force method) we would have a solution with a time complexity of Θ(n!). Solutions of this form scale rediculously as n - in this case the triange height - increases, and this is why problem 67 should not be possible with this method.

I then started thinking about directed acyclic graphs and the possibility of implementing a Dijkstra algorithm, which greatly excited me as I've never officially implemented one of these. Unfortunately I concocted another solution with the same time complexity - Θ(n²) - that was very easy to program.

<a href="https://github.com/AncientAbysswalker/Projekt-Euler/blob/master/Euler%20Projekt%20018%20-%20Maximum%20path%20sum%20I/Algo.png" target="_blank"><img src="https://github.com/AncientAbysswalker/Projekt-Euler/blob/master/Euler%20Projekt%20018%20-%20Maximum%20path%20sum%20I/Algo.png" title="Solution Method" /></a>

Looking at the above diagram we can see my method applied to the example. Starting from the bottom we move up to each node in the row above, adding the maximum of the two branching paths off those nodes from the bottom row to those nodes. This is shown as the green triangles in the diagram. We then move up and repeat untile we get to the head node. In my diagram I used blue to represent numbers where the left was added and red for where ther right was added. 

Observing the pattern we can easily determine the time complexity. Each triangle contains 3 computations, and the number of triangles is the depth of the computation row - 3,2,1 - which starts from n-1 where n is the triangle height. Therefore:

<a href="https://www.codecogs.com/eqnedit.php?latex=\frac{3n(n-1))}{2}\rightarrow&space;\Theta&space;(n^2)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\frac{3n(n-1))}{2}\rightarrow&space;\Theta&space;(n^2)" title="\frac{3n(n-1))}{2}\rightarrow \Theta (n^2)" /></a>