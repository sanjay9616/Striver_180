<h2><a href="https://leetcode.com/problems/search-a-2d-matrix/description/">12. Search a 2D Matrix</a></h2>

You are given an m x n integer matrix matrix with the following two properties:

An inversion is defined for a pair of integers in the array/list when the following two conditions are met.

A pair ('ARR[i]', 'ARR[j]') is said to be an inversion when:

1. Each row is sorted in non-decreasing order.</br>
2. The first integer of each row is greater than the last integer of the previous row.</br>

Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

**Example 1:**

![Screenshot from 2024-02-07 22-36-39](https://github.com/sanjay9616/Striver_180/assets/87460579/206eff28-78da-4966-99f5-7d0c7065d528)

**Input**: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3

**Output**: true

**Example 2:**

![Screenshot from 2024-02-07 22-38-06](https://github.com/sanjay9616/Striver_180/assets/87460579/a0cf7ded-b085-46db-9ebb-a016c6ed409c)

**Input**: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13

**Output**: false


**Constraints**:

    • m == matrix.length
    • n == matrix[i].length
    • 1 <= m, n <= 100
    • -10^4 <= matrix[i][j], target <= 10^4


