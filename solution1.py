# Approach 1: Using Recursion
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if (not root):
            return []
        return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)

# Time Coplexicity = O(N) => Result = Success
# Space Complexity = O(h) => height of the tree
