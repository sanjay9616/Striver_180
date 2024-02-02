### Approach 1: Transpose then Reverse individual rows

We first transpose the given matrix, and then reverse the content of individual rows to get the resultant 90 degree clockwise rotated matrix.


|1  2  3    |     1  4  7       |      7  4  1|
|           |                   |             | 
|4  5  6    |     2  5  8       |      8  5  2|
|           |                   |             |
|7  8  9    |     3  6  9       |      9  6  3|




| Algorithm              | Time Complexity   | Space Complexity  |
|----------------------- | ----------------- | ----------------- |
| Transpose->Reverse     | O(N<sup>2</sup>)  | O(1)              |

### Approach 2: Rotate Cycle Wise

Print the elements of the cycle in a clockwise direction i.e. An N x N matrix will have floor(N/2) square cycles.

For each square cycle, we swap the elements involved with the corresponding cell in the matrix in the clockwise direction. We just need a temporary variable for this.

| Algorithm              | Time Complexity   | Space Complexity |
|----------------------- | ----------------- | ---------------- |
| Rotate Cycle Wise | O(N<sup>2</sup>)  | O(1)             |


### Approach 3: Greedy Approach

| Algorithm       | Time Complexity          | Space Complexity (Worst Case) |
|---------------- | ------------------------ | ----------------------------- |
| Greedy Algo     | O(N)                     | O(N)                          |
