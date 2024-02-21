# Approach 3: Using Two Pointer Technique

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        curr1, curr2 = headA, headB
        if (curr1 is None or curr2 is None):
            return None
        while (curr1 != curr2):
            curr1 = curr1.next
            curr2 = curr2.next
            if (curr1 == curr2):
                return curr1
            if (curr1 is None):
                curr1 = headB
            if (curr2 is None):
                curr2 = headA
        return curr1

# Time Coplexicity = O(M + N) => Result = Success
# Space Complexity = O(1)