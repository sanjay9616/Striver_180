# Approach 1: Using DFS

class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        l = []

        def dfs(root, level, axis):
            if (root):
                l.append([level, axis, root.val])
                dfs(root.left, level + 1, axis - 1)
                dfs(root.right, level + 1, axis + 1)
            return
        dfs(root, 0, 0)
        # Sort it axis wise and then level wise Store all values with same column
        l = sorted(l, key=lambda x: (x[1], x[0], x[2]))
        d = {}
        for i, j, k in l:
            if (j in d):
                d[j].append(k)
            else:
                d[j] = [k]
        return list(d.values())

# Time Coplexicity = O(N) => Result = Success
# Space Complexity = O(h) => height of the tree
