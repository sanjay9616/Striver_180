# Approach 1: Using DFS

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if (not root):
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


# Time Coplexicity = O(N) => Result = Success
# Space Complexity = O(h) => height of the tree
