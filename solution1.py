# Approach 1: Using Recursion (DFS)
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isValid(root, leftRange, rightRange):
            if (not root):
                return True
            if (not (leftRange < root.val and rightRange > root.val)):
                return False
            return isValid(root.left, leftRange, root.val) and isValid(root.right, root.val, rightRange)
        return isValid(root, float('-inf'), float('inf'))

# Time Coplexicity = O(N) => Result = Success
# Space Complexity = O(1)
