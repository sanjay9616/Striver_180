# Approach 1: Using DFS

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        levelWiseNode = {}

        def dfs(root, level):
            if (root):
                if (level in levelWiseNode):
                    levelWiseNode[level].append(root.val)
                else:
                    levelWiseNode[level] = [root.val]
                dfs(root.left, level + 1)
                dfs(root.right, level + 1)
            return
        dfs(root, 0)
        res = []
        for level in sorted(levelWiseNode.keys()):
            res.append(levelWiseNode[level])
        return res


# Time Coplexicity = O(N) => Result = Success
# Space Complexity = O(h + 2^h) => height of the tree
