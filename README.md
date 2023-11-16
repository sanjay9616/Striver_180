<h2><a href="https://leetcode.com/problems/set-matrix-zeroes/description/">1. Set Matrix Zeroes</a></h2>

**Given an m x n integer matrix, if an element is 0, set its entire row and column to 0's.**

**You must do it in place.**


**Example 1:**

![Screenshot from 2023-11-16 18-05-02](https://github.com/sanjay9616/Striver_180/assets/87460579/5d20474d-666c-4551-b59f-f48b73e5e1b7)

**Input**: matrix = [[1,1,1],[1,0,1],[1,1,1]]
**Output**: [[1,0,1],[0,0,0],[1,0,1]]


**Example 2:**

![Screenshot from 2023-11-16 18-07-23](https://github.com/sanjay9616/Striver_180/assets/87460579/b0ed383d-c43f-4770-be3c-fe5e4ded302d)

**Input**: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
**Output**: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]

**Constraints**:

    • m == matrix.length
    • n == matrix[0].length
    • 1 <= m, n <= 200
    • -231 <= matrix[i][j] <= 231 – 1

Follow up:

    • A straightforward solution using O(mn) space is probably a bad idea.
    • A simple improvement uses O(m + n) space, but still not the best solution.
    • Could you devise a constant space solution?
