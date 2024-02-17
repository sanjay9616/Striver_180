# Approach 2: Using Two Pointer

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow = fast = head
        for i in range(n):
            fast = fast.next
        if(fast is None):
            return head.next
        while(fast.next):
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return head


# Time Coplexicity = O(N) => Result = Success
# Space Complexity = O(1)
