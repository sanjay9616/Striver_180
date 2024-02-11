<h2><a href="https://www.codingninjas.com/studio/problems/subarrays-with-xor-k_6826258?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf&leftPanelTabValue=PROBLEM">22. Subarrays with XOR ‘K’</a></h2>

Given an array ‘A’ consisting of ‘N’ integers and an integer ‘B’, find the number of subarrays of array ‘A’ whose bitwise XOR( ⊕ ) of all elements is equal to ‘B’.

A subarray of an array is obtained by removing some(zero or more) elements from the front and back of the array.


**Example 1:**

**Input**: a = [1, 2, 3, 2], b = 2

**Output**: 3

**Explanation**: Explanation: Subarrays have bitwise xor equal to ‘2’ are: [1, 2, 3, 2], [2], [2].

**Example 2:**

**Input**: a = [1, 2, 3, 3], b = 3

**Output**: 4

**Example 3:**

**Input**: a = [1, 3, 3, 3, 5], b = 6

**Output**: 2



**Constraints**:

    • 1 <= N <= 10^3
    • 1 <= A[i], B <= 10^9