# Approach 1: Using DFS
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def dfs(left, right):
            if (not left and not right):
                return True
            if (not left or not right):
                return False
            return left.val == right.val and dfs(left.left, right.right) and dfs(left.right, right.left)
        return dfs(root.left, root.right)

# Time Coplexicity = O(N) => Result = Success
# Space Complexity = O(h)
