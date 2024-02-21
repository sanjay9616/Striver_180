# Approach 1: Node assignment

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next


# Time Coplexicity = O(1) => Result = Success
# Space Complexity = O(1)
