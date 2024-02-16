# Approach 1: Using Iterative Method
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        while(head):
            nxt = head.next
            head.next = prev
            prev = head
            head = nxt
        # return prev
        # OR
        head = prev
        return head


# Time Coplexicity = O(N) => Result = Success
# Space Complexity = O(1)
