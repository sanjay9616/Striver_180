# Approach 1: By Traversing On Larger List

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy = curr = ListNode(0)
        while l1 or l2:
            v1 = v2 = 0
            if(l1):
                v1 = l1.val
                l1 = l1.next
            if(l2):
                v2 = l2.val
                l2 = l2.next
            carry, nodeValue = (v1+v2+carry) // 10, (v1+v2+carry) % 10
            curr.next = ListNode(nodeValue)
            curr = curr.next
        if(carry):
            curr.next = ListNode(carry)
        return dummy.next


# Time Coplexicity = max(O(N), O(M)) = O(N) => Result = Success
# Space Complexity = O(1)
