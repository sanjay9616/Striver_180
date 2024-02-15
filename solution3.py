# Approach 1: Using Using the last Index

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right, n = 0, 0, len(s)
        res = 0
        hasMap = {}
        while(right < n):
            if(s[right] in hasMap):
                left = max(left, hasMap[s[right]] + 1)
            hasMap[s[right]] = right
            res = max(res, right - left + 1)
            right += 1
        return res

# Using Using the last Index
# Time Coplexicity = O(N) => Result = Success
# Space Complexity = O(N)

