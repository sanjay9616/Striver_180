<h2><a href="https://www.geeksforgeeks.org/problems/bfs-traversal-of-graph/1">147. BFS of graph</a></h2>

Given a directed graph. The task is to do Breadth First Traversal of this graph starting from 0.
Note: One can move from node u to node v only if there's an edge from u to v. Find the BFS traversal of the graph starting from the 0th vertex, from left to right according to the input graph. Also, you should only take nodes directly or indirectly connected from Node 0 in consideration.

**Example 1**:

<img src="https://media.geeksforgeeks.org/img-practice/PROD/addEditProblem/700217/Web/Other/e0eb5630-5d6c-493a-9b1e-d16d40f10b01_1685086421.png" alt="not found">

**Input**: V = 5, E = 4, adj = {{1,2,3},{},{4},{},{}}

**Output**: 0 1 2 3 4

**Explanation**:
0 is connected to 1 , 2 , 3. </br>
2 is connected to 4. </br>
so starting from 0, it will go to 1 then 2 </br>
then 3. After this 2 to 4, thus bfs will be 0 1 2 3 4. </br>

**Example 2**:

<img src="https://media.geeksforgeeks.org/img-practice/PROD/addEditProblem/700217/Web/Other/e0eb5630-5d6c-493a-9b1e-d16d40f10b01_1685086421.png" alt="not found">

**Input**: V = 3, E = 2, adj = {{1,2},{},{}}

**Output**: 0 1 2

**Explanation**:
0 is connected to 1 , 2. </br>
so starting from 0, it will go to 1 then 2, </br>
thus bfs will be 0 1 2. </br>


**Constraints**:

    • 1 ≤ V, E ≤ 10^4
    • Expected Time Complexity: O(V + E)
    • Expected Auxiliary Space: O(V)