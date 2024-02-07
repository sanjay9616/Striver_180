<h2><a href="https://www.codingninjas.com/studio/problems/count-inversions_615">11. Count Inversions</a></h2>

For a given integer array/list 'ARR' of size 'N' containing all distinct values, find the total number of 'Inversions' that may exist.

An inversion is defined for a pair of integers in the array/list when the following two conditions are met.

A pair ('ARR[i]', 'ARR[j]') is said to be an inversion when:

1. 'ARR[i] > 'ARR[j]'</br>
2. 'i' < 'j'</br>

**Example 1:**

**Input**: n = 3, arr = [3, 2, 1]

**Output**: 3

**Explanation**: We have a total of 3 pairs which satisfy the condition of inversion. (3, 2), (2, 1) and (3, 1).

**Example 1:**

**Input**: n = 5, arr = [2, 5, 1, 3, 4]

**Output**: 4

**Explanation**: We have a total of 4 pairs which satisfy the condition of inversion. (2, 1), (5, 1), (5, 3) and (5, 4).


**Constraints**:

    • 1 <= N <= 10^5
    • 1 <= ARR[i] <= 10^9


