# Approach 2: Floyd's Cycle-Finding algorithm
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or k == 0 or head.next is None:
            return head
        count = 1
        curr = head
        while (curr.next):
            count += 1
            curr = curr.next
        k = k % count
        newTail = head
        curr.next = head
        for i in range(count - k - 1):
            newTail = newTail.next
        newHead = newTail.next
        newTail.next = None
        return newHead

# Time Coplexicity = O(N) = O(N) => Result = Success
# Space Complexity = O(1)
