# Approach 3: Using Difference In Node Counts

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        count1, count2 = 0, 0
        curr1, curr2 = headA, headB
        while(curr1):
            count1 += 1
            curr1 = curr1.next
        while(curr2):
            count2 += 1
            curr2 = curr2.next
        curr1, curr2 = headA, headB
        if(count1 > count2):
            for i in range(count1 - count2):
                curr1 = curr1.next
        elif(count2 > count1):
            for i in range(count2 - count1):
                curr2 = curr2.next
        while(curr2 != curr1):
            curr1 = curr1.next
            curr2 = curr2.next
        return curr1

# Time Coplexicity = O(M + N) => Result = Success
# Space Complexity = O(1)