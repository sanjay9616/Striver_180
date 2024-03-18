<h2><a href="https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/description/">130. Predecessor And Successor In BST</a></h2>

You have been given a binary search tree of integers with ‘N’ nodes. You are also given 'KEY' which represents data of a node of this tree.

Your task is to return the predecessor and successor of the given node in the BST.

1. The predecessor of a node in BST is that node that will be visited just before the given node in the inorder traversal of the tree. If the given node is visited first in the inorder traversal, then its predecessor is NULL.

2. The successor of a node in BST is that node that will be visited immediately after the given node in the inorder traversal of the tree. If the given node is visited last in the inorder traversal, then its successor is NULL.

**Example 1**:

<img src="https://files.codingninjas.in/screenshot-14-5921.png" alt="not found">

**Input**: root = [15, 10, 20, 8, 12, 16, 25, -1, -1, -1, -1, -1, -1, -1, -1], key = 10

**Output**: [8, 12]

**Example 2**:

**Input**: root = [10, 5, -1, -1, -1], key = 5

**Output**: [-1, 10]


**Constraints**:

    • 1 <= N <= 10^4
    • 1 <= data <= 10^7