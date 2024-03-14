# Approach 1: Using DFS
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def getLeftView(root) -> list:
    res = []
    def dfs(root, level):
        if (root is None):
            return
        if (level == len(res)):
            res.append(root.data)
        dfs(root.left, level + 1)
        dfs(root.right, level + 1)
        return
    dfs(root, 0)
    return res


# Time Coplexicity = O(N) => Result = Success
# Space Complexity = O(h) => height of the tree
