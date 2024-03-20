# Approach 1: Using Stack #Revise
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        self.sum = 0

        def dfs(cur):
            left, leftMin, leftMax = dfs(cur.left) if cur.left else (
                0, float('inf'), float('-inf'))
            right, rightMin, rightMax = dfs(cur.right) if cur.right else (
                0, float('inf'), float('-inf'))
            if left is not None and right is not None:
                if cur.val > leftMax and cur.val < rightMin:
                    s = cur.val + left + right
                    self.sum = max(self.sum, s)
                    return s, min(cur.val, leftMin), max(cur.val, rightMax)
            return (None, None, None)
        dfs(root)
        return self.sum

# Time Coplexicity = O(N) => Result = Success
# Space Complexity = O(1) => height of the tree
