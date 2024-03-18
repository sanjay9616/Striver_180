# Approach 1: Using DFS
import sys


def floorInBST(root, X):
    if root is None:
        return sys.maxsize
    if root.data == X:
        return root.data
    if root.data > X:
        return floorInBST(root.left, X)
    floorValue = floorInBST(root.right, X)
    if floorValue <= X:
        return floorValue
    else:
        return root.data

## ----------------------- Iterative Solution -------------------------------##

def floorInBST(root, x):
    if not root:
        return -1
    while root:
        if root.data == x:
            return root.data
        if root.data < x:
            floor = root.data
            root = root.right
        else:
            root = root.left
    return floor

# Time Coplexicity = O(N) => Result = Success
# Space Complexity = O(h) => height of the tree
