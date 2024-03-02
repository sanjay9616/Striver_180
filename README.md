<h2><a href="https://www.codingninjas.com/studio/problems/rat-in-a-maze-_8842357?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf">57. Rat In a Maze</a></h2>

You are given a N*N maze with a rat placed at 'mat[0][0]'. Find all paths that rat can follow to reach its destination i.e. mat[N-1][N-1]. The directions in which the rat can move are 'U'(up), 'D'(down), 'L' (left), 'R' (right).

In the given maze, each cell can have a value of either 0 or 1. Cells with a value of 0 are considered blocked, which means the rat cannot enter or traverse through them. On the other hand, cells with a value of 1 are open, indicating that the rat is allowed to enter and move through those cells.


**Example**:

mat:{{1, 0, 0, 0},
     {1, 1, 0, 1},
     {1, 1, 0, 0},
     {0, 1, 1, 1}}

All possible paths are:</br>
DDRDRR (in red)</br>
DRDDRR (in green)</br>

<img src="https://files.codingninjas.in/untitled-21-28443.jpg" alt="not found">


**Explanation**: The given adjacency matrix tells us that 1 is connected to 2 and 2 is connected to 3. We can use three different colors  color all three nodes.
Hence we return true.