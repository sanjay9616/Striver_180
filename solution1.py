# Approach 1: Brute Force
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nodeValue = []
        while(head):
            nodeValue.append(head.val)
            head = head.next
        head = curr = ListNode(-1)
        n = len(nodeValue)
        for i in range(n//2, n, 1):
            curr.next = ListNode(nodeValue[i])
            curr = curr.next
        return head.next


# Time Coplexicity = O(N) => Result = Success
# Space Complexity = O(N)
