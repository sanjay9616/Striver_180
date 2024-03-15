# Approach 1: Using DFS

class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        levelWiseIndex = {}

        def dfs(root, level, index):
            if (root):
                if (level in levelWiseIndex):
                    levelWiseIndex[level].append(index)
                else:
                    levelWiseIndex[level] = [index]
                dfs(root.left, level + 1, 2 * index)
                dfs(root.right, level + 1, 2 * index + 1)
            return
        dfs(root, 0, 1)
        res = 0
        print(levelWiseIndex)
        for level in levelWiseIndex:
            res = max(
                res, max(levelWiseIndex[level]) - min(levelWiseIndex[level]) + 1)
        return res


# Time Coplexicity = O(N) => Result = Success
# Space Complexity = O(h + 2^h) => height of the tree
