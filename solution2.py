# Approach 1: Using Using Recursion

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if(head is None or head.next is None):
            return head
        rest = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return rest

# Time Coplexicity = O(N) => Result = Success
# Space Complexity = O(N)
