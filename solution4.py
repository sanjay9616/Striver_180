# Approach 1: Using Stack

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if(head is None):
            return head
        stack, temp = [], head
        while(temp):
            stack.append(temp)
            temp = temp.next
        head = temp = stack.pop()
        while(len(stack)):
            temp.next = stack.pop()
            temp = temp.next
        temp.next = None
        return head

# Time Coplexicity = O(2 * N) = O(N) => Result = Success
# Space Complexity = O(N)