# Approach 1: By Storing length
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        def distance(first, last):
            count = 1
            while (first != last):
                count += 1
                first = first.next
            return count
        first = last = head;
        prevCount, currCount = -1, 1
        while (currCount > prevCount and last) :
            prevCount = currCount
            last = last.next;
            currCount = distance(first, last)
        if (last is None):
            return False
        return True

# Time Coplexicity = O(N^2) => Result = Success
# Space Complexity = O(1)
