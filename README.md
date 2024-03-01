<h2><a href="https://www.geeksforgeeks.org/problems/subset-sums2234/1">47. Subset Sums</a></h2>

Given a list arr of N integers, return sums of all subsets in it.

**Example 1:**

**Input**: N = 2, arr[] = {2, 3}

**Output**: 0 2 3 5

**Explanation**:
When no elements is taken then Sum = 0. </br>
When only 2 is taken then Sum = 2.</br>
When only 3 is taken then Sum = 3.</br>
When element 2 and 3 are taken then </br>
Sum = 2+3 = 5.


**Example 2:**

**Input**: N = 3, {5, 2, 1}

**Output**: 0 1 2 3 5 6 7 8

**Your Task**: You don't need to read input or print anything. Your task is to complete the function subsetSums() which takes a list/vector and an integer N as an input parameter and return the list/vector of all the subset sums.

**Expected Time Complexity**: O(2^N)
**Expected Auxiliary Space**: O(2^N)

**Constraints**:

    • 1 <= N <= 15
    • 0 <= arr[i] <= 10^4