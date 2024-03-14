# Approach 1: Using DFS
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def dfs(root, level):
            if (not root):
                return
            if (level == len(res)):
                res.append(root.val)
            dfs(root.right, level + 1)
            dfs(root.left, level + 1)
        dfs(root, 0)
        return res


# Time Coplexicity = O(N) => Result = Success
# Space Complexity = O(h) => height of the tree
