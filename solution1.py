# Approach 1: Using DFS
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.difference = 0
        self.isBalanced = True

        def dfs(root):
            if (not root):
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            self.difference = abs(left - right)
            if (self.difference >= 2):
                self.isBalanced = False
            return 1 + max(left, right)
        dfs(root)
        return self.isBalanced

# Time Coplexicity = O(N) => Result = Success
# Space Complexity = O(h) => height of the tree
