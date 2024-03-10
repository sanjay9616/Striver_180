# Approach 1: Brute Force

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n1, n2 = len(haystack), len(needle)
        for i in range(n1 - n2 + 1):
            if (needle == haystack[i:i+n2]):
                return i
        return -1

# Time Coplexicity = O(N) => Result = Success
# Space Complexity = O(1)
