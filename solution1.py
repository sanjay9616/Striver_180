# Approach 1: Brute Force (Using Hashing)
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if (head is None or k == 0 or head.next is None):
            return head
        nodeValue = []
        while (head):
            nodeValue.append(head.val)
            head = head.next
        n = len(nodeValue)
        for i in range(k % n):
            nodeValue = nodeValue[n - 1:] + nodeValue[:n-1]
        dummy = curr = ListNode(-1)
        for i in nodeValue:
            curr.next = ListNode(i)
            curr = curr.next
        return dummy.next

# Time Coplexicity = O(N) = O(N) => Result = Success
# Space Complexity = O(N)
