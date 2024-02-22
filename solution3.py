# Approach 3: By Modification In Node Structure
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        curr = head
        while(curr):
            if(curr.val == 'visited'):
                return True
            curr.val = 'visited'
            curr = curr.next
        return False

# Time Coplexicity = O(N) => Result = Success
# Space Complexity = O(1)