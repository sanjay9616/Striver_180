# Approach 2: Using Hashing

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        hs = set()
        while(headA):
            hs.add(headA)
            headA = headA.next
        while(headB):
            if(headB in hs):
                return headB
            headB = headB.next
        return None

# Time Coplexicity = O(N) => Result = Success
# Space Complexity = O(N)