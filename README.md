<h2><a href="https://www.geeksforgeeks.org/problems/topological-sort/1">149. Topological sort</a></h2>

Given a Directed Acyclic Graph (DAG) with V vertices and E edges, Find any Topological Sorting of that Graph.

**Example 1**:

<img src="https://media.geeksforgeeks.org/img-practice/PROD/addEditProblem/700255/Web/Other/24aa5d54-bc1f-489c-bd2d-ad02ddccdf31_1684492511.png" alt="not found">

**Output**: 1

**Explanation**:
The output 1 denotes that the order is </br>
valid. So, if you have, implemented </br>
your function correctly, then output </br>
would be 1 for all test cases. </br>
One possible Topological order for the </br>
graph is 3, 2, 1, 0.

**Example 2**:

<img src="https://media.geeksforgeeks.org/img-practice/PROD/addEditProblem/700255/Web/Other/c35bb1d1-130c-49aa-a17e-118181d7bdcd_1684492512.png" alt="not found">

**Output**: 1

**Explanation**:
The output 1 denotes that the order is </br>
valid. So, if you have, implemented </br>
your function correctly, then output </br>
would be 1 for all test cases. </br>
One possible Topological order for the </br>
graph is 5, 4, 2, 1, 3, 0.


**Constraints**:

    • 2 ≤ V ≤ 10^4
    • 1 ≤ E ≤ (N*(N-1))/2
    • Expected Time Complexity: O(V + E).
    • Expected Auxiliary Space: O(V).