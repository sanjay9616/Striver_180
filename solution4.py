# Approach 3: Using Floyd’s Cycle-Finding Algorithm
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        while(fast and fast.next):
            slow = slow.next
            fast = fast.next.next
            if(slow == fast):
                return True
        return False

# Time Coplexicity = O(N) => Result = Success
# Space Complexity = O(1)