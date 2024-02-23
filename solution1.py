# Approach 1: Brute Force
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        nodeValue = []
        while (head):
            nodeValue.append(head.val)
            head = head.next
        for i in range(0, len(nodeValue)//2, 1):
            if (nodeValue[i] != nodeValue[len(nodeValue) - i - 1]):
                return False
        return True

# Time Coplexicity = O(N + N//2) = O(N) => Result = Success
# Space Complexity = O(N)
