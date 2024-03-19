# Approach 1: Using DFS
import sys


def KthLargestNumber(root, k):
    def dfs(root):
        if (not root):
            return []
        return dfs(root.left) + [root.data] + dfs(root.right)
    arr = dfs(root)
    return arr[len(arr) - k] if (len(arr) >= k) else -1

# Time Coplexicity = O(N) => Result = Success
# Space Complexity = O(h) => height of the tree
