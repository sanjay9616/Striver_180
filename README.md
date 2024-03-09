<h2><a href="https://www.codingninjas.com/studio/problems/immediate-smaller-element-_1062597?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf">78. Immediate Smaller Element</a></h2>

You are given an integer array 'a' of size 'n'.

For each element in the array, check whether the immediate right element of the array is smaller or not.

If the next element is smaller, update the current index to that element. If not, then -1. The last element does not have any elements on its right.

**Example** :

Input: 'a' = [4, 7, 8, 2, 3, 1] </br>
Output: Modified array 'a' = [-1, -1, 2, -1, 1, -1] </br>
Explanation: In the array 'a': </br>
4 has 7 on its right. Since 7 is not smaller, we update 4 to -1. </br>
7 has 8 on its right. Since 8 is not smaller, we update 7 to -1. </br>
8 has 2 on its right. Since 2 is smaller than 8, we update 8 to 2. </br>
2 has 3 on its right. Since 3 is not smaller, we update 2 to -1. </br>
3 has 1 on its right. Since 1 is smaller than 3, we update 3 to 1. </br>
1 does not have any element on right. So we update 1 to -1. </br>

**Example 1**:

**Input** nums1 = [4, 7, 8, 2, 3, 1]

**Output**: [-1, -1, 2, -1, 1, -1 ]

**Explanation**: In the array 'a': </br>
4 has 7 on its right. Since 7 is not smaller, we update 4 to -1. </br>
7 has 8 on its right. Since 8 is not smaller, we update 7 to -1. </br>
8 has 2 on its right. Since 2 is smaller than 8, we update 8 to 2. </br>
2 has 3 on its right. Since 3 is not smaller, we update 2 to -1. </br>
3 has 1 on its right. Since 1 is smaller than 3, we update 3 to 1. </br>
1 does not have any element on right. So we update 1 to -1. </br>

**Example 2**:

**Input** nums1 = [1, 2, 3, 4]

**Output**: [-1, -1, -1, -1 ]

**Example 3**:

**Input** nums1 = [4, 3, 2, 1]

**Output**: [3, 2, 1, -1]

**Constraints**:

    • 1 <= 'n' <= 10 ^ 5
    • 1 <= 'a[i]' <= 10 ^ 9
    • Time Limit : 1 sec
    • The expected time complexity is O(n).