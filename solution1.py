# Approach 1: Using Recursion (DFS) ## Solve Again
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        if (not preorder):
            return None
        root = TreeNode(preorder[0])
        i = 1
        while (i < len(preorder) and preorder[0] > preorder[i]):
            i += 1
        root.left = self.bstFromPreorder(preorder[1:i])
        root.right = self.bstFromPreorder(preorder[i:])
        return root

# Time Coplexicity = O(N) => Result = Success
# Space Complexity = O(h)
