# Approach 1: Using DFS
import sys


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def dfs(root):
            if (not root):
                return []
            return dfs(root.left) + [root.val] + dfs(root.right)
        return dfs(root)[k - 1]

# Time Coplexicity = O(N) => Result = Success
# Space Complexity = O(h) => height of the tree
