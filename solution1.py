# Approach 1: Using Recursion
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if (not root):
            return []
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)


# Time Coplexicity = O(N) => Result = Success
# Space Complexity = O(h) => height of the tree
