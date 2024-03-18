## ----------- Recursive ----------- ##

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if (p.val > root.val and q.val > root.val):
            return self.lowestCommonAncestor(root.right, p, q)
        elif (p.val < root.val and q.val < root.val):
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return root

## ----------- Iterative ----------- ##

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        while (root):
            if (p.val > root.val and q.val > root.val):
                root = root.right
            elif (p.val < root.val and q.val < root.val):
                root = root.left
            else:
                return root

# Time Coplexicity = O(h) => Result = Success
# Space Complexity = O(1) => height of the tree
