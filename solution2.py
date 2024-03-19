# Approach 1: Using DFS

class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        def dfs(root, k, seen):
            if(not root):
                return None
            if(k - root.val in seen):
                return True
            seen.add(root.val)
            left = dfs(root.left, k, seen)
            right = dfs(root.right, k, seen)
            return left or right
        return dfs(root, k, set())

# Time Coplexicity = O(N) => Result = Success
# Space Complexity = O(N) => height of the tree