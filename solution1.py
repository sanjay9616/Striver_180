# Approach 1: Brute Force (Using Hashing)
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        visitedNodes = set()
        while (head):
            if (head in visitedNodes):
                return head
            visitedNodes.add(head)
            head = head.next
        return None

# Time Coplexicity = O(N) = O(N) => Result = Success
# Space Complexity = O(N)
