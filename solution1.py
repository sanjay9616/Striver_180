# Approach 1: Using DFS
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if (not p and not q):  # if both trees are empty
            return True
        if (not p or not q):  # If one tree is empty while the other is not
            return False
        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

# Time Coplexicity = O(N) => Result = Success
# Space Complexity = O(h) => height of the tree
