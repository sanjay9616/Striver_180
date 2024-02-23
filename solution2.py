# Approach 2: Floyd's Cycle-Finding algorithm
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        while (fast and fast.next):
            slow, fast = slow.next, fast.next.next
            if (slow == fast):  # there is a cycle
                slow = head
                while (slow != fast):
                    slow, fast = slow.next, fast.next
                return slow
        return None
# Time Coplexicity = O(N) = O(N) => Result = Success
# Space Complexity = O(N)
