# Approach 1: Using DFS
import sys


def findCeil(root, x):
    if root is None:
        return -1
    if root.data == x:
        return root.data
    if root.data < x:
        return findCeil(root.right, x)
    ceilValue = findCeil(root.left, x)
    if ceilValue >= x:
        return ceilValue
    else:
        return root.data

## ----------------------- Iterative Solution -------------------------------##


def findCeil(root, x):
    if (not root):
        return -1
    ceil = -1
    while (root):
        if (root.data == x):
            return root.data
        if (root.data > x):
            ceil = root.data
            root = root.left
        else:
            root = root.right
    return ceil

# Time Coplexicity = O(N) => Result = Success
# Space Complexity = O(h) => height of the tree
