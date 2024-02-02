### Approach 1: Transpose then Reverse individual rows

We first transpose the given matrix, and then reverse the content of individual rows to get the resultant 90 degree clockwise rotated matrix.

| Algorithm              | Time Complexity   | Space Complexity  |
|----------------------- | ----------------- | ----------------- |
| Transpose->Reverse     | O(N<sup>2</sup>)  | O(1)              |

### Approach 2: Rotate Cycle Wise

Print the elements of the cycle in a clockwise direction i.e. An N x N matrix will have floor(N/2) square cycles.

For each square cycle, we swap the elements involved with the corresponding cell in the matrix in the clockwise direction. We just need a temporary variable for this.

| Algorithm              | Time Complexity   | Space Complexity |
|----------------------- | ----------------- | ---------------- |
| Rotate Cycle Wise | O(N<sup>2</sup>)  | O(1)             |


### Approach 3: The approach is based on the pattern made by indices after rotating the matrix. Consider the following illustration to have a clear insight into it.

After rotating the matrix by 90 degrees in clockwise direction, indices transform into

00 01 02         20 10 00
10 11 12 ----->  21 11 01
20 21 22         22 12 02


| Algorithm       | Time Complexity          | Space Complexity (Worst Case) |
|---------------- | ------------------------ | ----------------------------- |
| ===========     | O(N)                     | O(N)                          |
