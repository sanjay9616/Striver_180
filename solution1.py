# Approach 1: Using DFS
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        levelWiseNode = {}

        def dfs(root, level):
            if (root):
                if (level in levelWiseNode):
                    levelWiseNode[level].append(root.val)
                else:
                    levelWiseNode[level] = [root.val]
                dfs(root.left, level + 1)
                dfs(root.right, level + 1)
        dfs(root, 0)
        res = []
        for level in sorted(levelWiseNode.keys()):
            if (level % 2 != 0):
                res.append(levelWiseNode[level][::-1])
            else:
                res.append(levelWiseNode[level])
        return res

# Time Coplexicity = O(N * log(N)) => Result = Success
# Space Complexity = O(h + 2^n)
