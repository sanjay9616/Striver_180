<h2><a href="https://leetcode.com/problems/reverse-pairs/description/">17. Reverse Pairs</a></h2>

Given an integer array nums, return the number of reverse pairs in the array.

A reverse pair is a pair (i, j) where: </br>
1. 0 <= i < j < nums.length and </br>
2. nums[i] > 2 * nums[j]

**Example 1:**

**Input**: nums = [1,3,2,3,1]

**Output**: 2

**Explanation**: The reverse pairs are: </br>
1. (1, 4) --> nums[1] = 3, nums[4] = 1, 3 > 2 * 1 </br>
2. (3, 4) --> nums[3] = 3, nums[4] = 1, 3 > 2 * 1 </br>


**Example 1:**

**Input**: nums = [2,4,3,5,1]

**Output**: 3

**Explanation**: The reverse pairs are: </br>
1. (1, 4) --> nums[1] = 4, nums[4] = 1, 4 > 2 * 1 </br>
2. (2, 4) --> nums[2] = 3, nums[4] = 1, 3 > 2 * 1 </br>
3. (3, 4) --> nums[3] = 5, nums[4] = 1, 5 > 2 * 1 </br>


**Constraints**:

    • 1 <= nums.length <= 5 * 10^4
    • -2^31 <= nums[i] <= 2^31 - 1
