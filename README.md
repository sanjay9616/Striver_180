<h2><a href="https://www.geeksforgeeks.org/problems/k-th-element-of-two-sorted-array1317/1">64. K-th element of two Arrays</a></h2>

Given two sorted arrays arr1 and arr2 of size N and M respectively and an element K. The task is to find the element that would be at the kth position of the final sorted array.

**Example 1**:

**Input**: arr1[] = {2, 3, 6, 7, 9}, arr2[] = {1, 4, 8, 10}, k = 5

**Output**: 6

**Expanation**: The final sorted array would be - {1, 2, 3, 4, 6, 7, 8, 9, 10}, The 5th element of this array is 6.

**Example 2**:

**Input**: arr1[] = {100, 112, 256, 349, 770}, arr2[] = {72, 86, 113, 119, 265, 445, 892}, k = 7

**Output**: 256

**Explanation**: Final sorted array is - {72, 86, 100, 112,113, 119, 256, 265, 349, 445, 770, 892}, 7th element of this array is 256.

**Constraints**:

    • 1 <= N, M <= 10^6
    • 0 <= arr1i, arr2i < INT_MAX
    • 1 <= K <= N+M
    • Expected Time Complexity: O(Log(N) + Log(M))
    • Expected Auxiliary Space: O(Log (N))
