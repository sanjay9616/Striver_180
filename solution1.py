# Approach 1: Using DFS
def predecessorSuccessor(root, key):
    def inorder(root):
        if (not root):
            return []
        return inorder(root.left) + [root.data] + inorder(root.right)
    inorderArray = inorder(root)
    predecessor = -1
    successor = -1
    for i in range(len(inorderArray)):
        if inorderArray[i] < key:
            predecessor = inorderArray[i]
    for i in range(len(inorderArray) - 1, -1, -1):
        if inorderArray[i] > key:
            successor = inorderArray[i]
    return (predecessor, successor)

# Time Coplexicity = O(N) => Result = Success
# Space Complexity = O(h) => height of the tree
