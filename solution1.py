# Approach 1: Briute Force

class Solution:
    def longestPalindrome(self, s: str) -> str:
        res, maxLength, n = "", 0, len(s)
        for i in range(1, n + 1):
            for j in range(n - i + 1):
                if (s[j:j+i] == s[j:j+i][::-1] and len(s[j:j+i]) > maxLength):
                    maxLength = len(s[j:j+i])
                    res = s[j:j+i]
        return res


# Time Coplexicity = O(N^3) => Result = Success
# Space Complexity = O(1)
