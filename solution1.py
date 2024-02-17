# Approach 1: Brute Force

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        nodeValue = []
        curr, count = head, 0
        while(curr):
            count += 1
            nodeValue.append(curr.val)
            curr = curr.next
        nodeValue.pop(count - n)
        count =- 1
        dummy = curr = ListNode(-1)
        for i in nodeValue:
            curr.next = ListNode(i)
            curr = curr.next
        return dummy.next


# Time Coplexicity = O(N) => Result = Success
# Space Complexity = O(N)
