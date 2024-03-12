# Approach 1: Using Recursion
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if (not root):
            return []
        return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]


# Time Coplexicity = O(N) => Result = Success
# Space Complexity = O(h) => height of the tree
