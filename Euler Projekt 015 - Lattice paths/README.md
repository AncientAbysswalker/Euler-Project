# Lattice paths

## Problem Statement

Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

<a href="https://projecteuler.net/project/images/p015.gif" target="_blank"><img src="https://projecteuler.net/project/images/p015.gif" title="Lattice" /></a>

How many such routes are there through a 20×20 grid?

## Solution
Very simple, I remember doing these in highschool. The number of lattice paths to any point on these grids is simple the Pascal's triangle rotated 45 degrees - with special consideration on how to map to the points on the traingle given the rotation. Also make sure to remember an AxA grid has A+1 paths in each direction you can traverse.

<a href="https://github.com/AncientAbysswalker/Projekt-Euler/blob/master/Euler%20Projekt%20015%20-%20Lattice%20paths/Example.png"><img src="https://github.com/AncientAbysswalker/Projekt-Euler/blob/master/Euler%20Projekt%20015%20-%20Lattice%20paths/Example.png" title="Lattice" /></a>
