# Approach 1: Using DFS

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = root.val
        def dfs(root):
            if(not root):
                return 0
            leftMaxSum = max(0, dfs(root.left)) # if left max sum negative ignore
            rightMaxSum = max(0, dfs(root.right))
            self.res = max(self.res, leftMaxSum + rightMaxSum + root.val)
            return  max(leftMaxSum, rightMaxSum) + root.val
        dfs(root)
        return self.res

# Time Coplexicity = O(N) => Result = Success
# Space Complexity = O(h)
