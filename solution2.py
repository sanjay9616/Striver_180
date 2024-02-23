# Approach 2: Using Stack
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        stack = []
        curr = head
        while(curr):
            stack.append(curr.val)
            curr = curr.next
        while(head):
            if(stack.pop() != head.val):
                return False
            head = head.next
        return True

# Time Coplexicity = O(N + N) = O(N) => Result = Success
# Space Complexity = O(N)