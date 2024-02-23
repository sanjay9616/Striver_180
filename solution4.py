# Approach 2: Using Stack
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        while(fast and fast.next):
            slow, fast = slow.next, fast.next.next
        prev = None
        while(slow):
            nxt = slow.next
            slow.next = prev
            prev = slow
            slow = nxt
        while(prev):
            if(head.val != prev.val):
                return False
            head, prev = head.next, prev.next
        return True

# Time Coplexicity = O(N + N + N) = O(N) => Result = Success
# Space Complexity = O(1)