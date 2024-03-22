<h2><a href="https://www.geeksforgeeks.org/problems/depth-first-traversal-for-a-graph/1">146. DFS of Graph</a></h2>

You are given a connected undirected graph. Perform a Depth First Traversal of the graph.

**Note**: Use the recursive approach to find the DFS traversal of the graph starting from the 0th vertex from left to right according to the graph.

**Example 1**:

<img src="https://media.geeksforgeeks.org/img-practice/graph-1659528381.png" alt="not found">

**Input**: V = 5 , adj = [[2,3,1] , [0], [0,4], [0], [2]]

**Output**: 0 2 4 3 1

**Explanation**:
0 is connected to 2, 3, 1. </br>
1 is connected to 0. </br>
2 is connected to 0 and 4. </br>
3 is connected to 0. </br>
4 is connected to 2. </br>
so starting from 0, it will go to 2 then 4, </br>
and then 3 and 1. </br>
Thus dfs will be 0 2 4 3 1. </br>

**Example 2**:

<img src="https://media.geeksforgeeks.org/img-practice/graph(1)-1659528893.png" alt="not found">

**Input**: V = 4, adj = [[1,3], [2,0], [1], [0]]

**Output**: 0 1 2 3

**Explanation**:
0 is connected to 1 , 3. </br>
1 is connected to 0, 2. </br>
2 is connected to 1. </br>
3 is connected to 0. </br>
so starting from 0, it will go to 1 then 2 </br>
then back to 0 then 0 to 3 </br>
thus dfs will be 0 1 2 3. </br>


**Constraints**:

    • 1 ≤ V, E ≤ 10^4
    • Expected Time Complexity: O(V + E)
    • Expected Auxiliary Space: O(V)