# Approach 1: Using DFS

def getTreeTraversal(root):
    def inOrderTraversal(root):
        if (not root):
            return []
        return inOrderTraversal(root.left) + [root.data] + inOrderTraversal(root.right)

    def preOrderTraversal(root):
        if (not root):
            return []
        return [root.data] + preOrderTraversal(root.left) + preOrderTraversal(root.right)

    def postOrderTraversal(root):
        if (not root):
            return []
        return postOrderTraversal(root.left) + postOrderTraversal(root.right) + [root.data]
    return [inOrderTraversal(root), preOrderTraversal(root), postOrderTraversal(root)]
    pass

# Time Coplexicity = O(N) => Result = Success
# Space Complexity = O(h) => height of the tree
