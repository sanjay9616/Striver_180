# Approach 2: Using Expansion From Center

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if (len(s) <= 1):
            return s

        def expandFromCenter(left, right):
            while (left >= 0 and right < len(s) and s[left] == s[right]):
                left -= 1
                right += 1
            return s[left + 1:right]
        res = s[0]
        for i in range(len(s) - 1):
            odd = expandFromCenter(i, i)
            even = expandFromCenter(i, i + 1)
            if (len(odd) > len(res)):
                res = odd
            if (len(even) > len(res)):
                res = even
        return res

# Time Coplexicity = O(N^2) => Result = Success
# Space Complexity = O(1)
