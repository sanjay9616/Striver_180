# Approach 1: Using Two Nested Loops (Brute Force)

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        while(headA):
            tempB = headB
            while(tempB):
                if(headA == tempB):
                    return tempB
                tempB = tempB.next
            headA = headA.next
        return None

# Time Coplexicity = O(M * N) => Result = TLE
# Space Complexity = O(1)
