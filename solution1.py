# Approach 1: Using DFS
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if (not root):
            return None
        if (root == p or root == q):
            return root  # I see one of the targets! I will inform my caller!
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if (not left):
            return right  # Didnt find anything in the left, must be in right
        if (not right):
            return left  # Didnt find anything in the right, must be in the left
        return root  # Found something in both! Hence this is the one!

# Time Coplexicity = O(N) => Result = Success
# Space Complexity = O(h) => height of the tree
