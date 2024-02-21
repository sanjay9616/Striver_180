<h2><a href="https://leetcode.com/problems/delete-node-in-a-linked-list/description/">28. Delete Node in a Linked List</a></h2>

There is a singly-linked list head and we want to delete a node node in it.

You are given the node to be deleted node. You will not be given access to the first node of head.

All the values of the linked list are unique, and it is guaranteed that the given node node is not the last node in the linked list.

Delete the given node. Note that by deleting the node, we do not mean removing it from memory. We mean:

1. The value of the given node should not exist in the linked list. </br>
2. The number of nodes in the linked list should decrease by one. </br>
3. All the values before node should be in the same order. </br>
4. All the values after node should be in the same order. </br>

**Custom testing:**

1. For the input, you should provide the entire linked list head and the node to be given node. node should not be the last node of the list and should be an actual node in the list.</br>
2. We will build the linked list and pass the node to your function.</br>
3. The output will be the entire list after calling your function.</br>

**Example 1:**

<img src="https://assets.leetcode.com/uploads/2020/09/01/node1.jpg" alt="Not Found">

**Input**: head = [4,5,1,9], node = 5

**Output**: [4,1,9]

**Explanation**: You are given the second node with value 5, the linked list should become 4 -> 1 -> 9 after calling your function.

**Example 2:**

<img src="https://assets.leetcode.com/uploads/2020/09/01/node2.jpg" alt="Not Found">

**Input**: head = [4,5,1,9], node = 1

**Output**: [4,5,9]

**Explanation**: You are given the third node with value 1, the linked list should become 4 -> 5 -> 9 after calling your function.


**Constraints**:

    • The number of the nodes in the given list is in the range [2, 1000].
    • -1000 <= Node.val <= 1000
    • The value of each node in the list is unique.
    • The node to be deleted is in the list and is not a tail node.