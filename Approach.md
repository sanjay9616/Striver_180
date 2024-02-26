### Approach 1: Greedy approach

The idea is to solve the problem using the greedy approach which is the same as <a href="https://www.geeksforgeeks.org/activity-selection-problem-greedy-algo-1/">Activity Selection Problem</a> i.e sort the meetings by their finish time and then start selecting meetings, starting with the one with least end time and then select other meetings such that the start time of the current meeting is greater than the end time of last meeting selected

**Following are some standard algorithms that are Greedy algorithms**
    • Kruskal’s Minimum Spanning Tree (MST)
    • Prim’s Minimum Spanning Tree
    • Dijkstra’s Shortest Path
    • Huffman Coding:
    • Dijkstra’s Shortest Path


| Algorithm              | Time Complexity   | Space Complexity  |
|----------------------- | ----------------- | ----------------- |
| Brute Force            | O(N log N)        | O(N)              |



