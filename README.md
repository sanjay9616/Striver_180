<h2><a href="https://www.codingninjas.com/studio/problems/m-coloring-problem_981273?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf">56. M-Coloring Problem</a></h2>

You are given an undirected graph as an adjacency matrix consisting of 'v' vertices and an integer 'm'.

You need to return 'YES' if you can color the graph using at most 'm' colors so that no two adjacent vertices are the same. Else, return 'NO'.

**For example**:

**Input**:</br>
If the given adjacency matrix is:</br>
[0 1 0]</br>
[1 0 1]</br>
[0 1 0] and 'm' = 3.</br>

<img src="https://files.codingninjas.in/ex1-28434.png" alt="not found">

**Output**: YES

**Explanation**: The given adjacency matrix tells us that 1 is connected to 2 and 2 is connected to 3. We can use three different colors  color all three nodes.
Hence we return true.


**Example 1:**

**Input**:
3 2 </br>
0 1 0 </br>
1 0 1 </br>
0 1 0 </br>

**Output**: NO

**Constraints**:

    • 1 ≤ v ≤ 20
    • 1 ≤ m ≤ v
    • Time Limit: 1 sec