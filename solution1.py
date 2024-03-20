# Approach 1: Using Stack
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if (not root):
            return 'None'
        return str(root.val) + ',' + self.serialize(root.left) + ',' + self.serialize(root.right)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        treeList = data.split(',')

        def traversal():
            nextNode = treeList.pop(0)
            if (nextNode == "None"):
                return None
            newRoot = TreeNode(int(nextNode))
            newRoot.left = traversal()
            newRoot.right = traversal()
            return newRoot
        return traversal()

# Time Coplexicity = O(N) => Result = Success
# Space Complexity = O(1) => height of the tree
