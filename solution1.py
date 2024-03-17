# Approach 1: Using Recursion (DFS) ## Solve Again
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if (root and root.val < val):
            return self.searchBST(root.right, val)
        elif (root and root.val > val):
            return self.searchBST(root.left, val)
        else:
            return root
# Time Coplexicity = O(log(N)) => Result = Success
# Space Complexity = O(1)
