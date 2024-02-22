# Approach 2: Using Hashing
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visitedNodes, curr = set(), head
        while(curr):
            if(curr in visitedNodes):
                return True
            visitedNodes.add(curr)
            curr = curr.next
        return False


# Time Coplexicity = O(N) => Result = Success
# Space Complexity = O(N)