# Approach 1: Brute Force
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        nodeValue = []
        curr = head
        while(curr):
            nodeValue.append(curr.val)
            curr = curr.next
        i = 0
        while(i < len(nodeValue)):
            if(i+k < len(nodeValue)+1):
                nodeValue[i:i+k] = nodeValue[i:i+k][::-1]
            i += k
        dummy = curr = ListNode(-1)
        for i in nodeValue:
            curr.next = ListNode(i)
            curr = curr.next
        return dummy.next

# Time Coplexicity = O(N^2) => Result = Success
# Space Complexity = O(N)
