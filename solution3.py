# Approach 1: Two Pointer
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        countNode = 0
        curr = head
        while(curr):
            countNode += 1
            curr = curr.next
        curr = head
        count = 0
        while(curr):
            if(count == countNode//2):
                head = curr
                return head
            count += 1
            curr = curr.next

# Time Coplexicity = O(N) => Result = Success
# Space Complexity = O(1)

