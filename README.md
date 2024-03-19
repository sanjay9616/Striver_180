<h2><a href="https://leetcode.com/problems/kth-smallest-element-in-a-bst/submissions/1208281475/">133. Kth Smallest Element in a BST</a></h2>

Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

**Example 1**:

<img src="https://assets.leetcode.com/uploads/2021/01/28/kthtree1.jpg" alt="not found">

**Input**: root = [3,1,4,null,2], k = 1

**Output**: 1

**Example 2**:

<img src="https://assets.leetcode.com/uploads/2021/01/28/kthtree2.jpg" alt="not found">

**Input**: root = [5,3,6,2,4,null,null,1], k = 3

**Output**: 3


**Constraints**:

    • The number of nodes in the tree is n.
    • 1 <= k <= n <= 10^4
    • 0 <= Node.val <= 10^4

**Follow up**: If the BST is modified often (i.e., we can do insert and delete operations) and you need to find the kth smallest frequently, how would you optimize?