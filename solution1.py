# Approach 1: Using Sliding Window in O(N^3) time

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        def isUniqueSubString(subString):
            # there are 256 ASCII characters
            visited = [False] * (256)
            for i in subString:
                if(visited[ord(i)] == True):
                    return False
                visited[ord(i)] = True
            return True
        res = 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                if(isUniqueSubString(s[i:j+1])):
                    res = max(res, len(s[i:j+1]))
        return res

# Using Sliding Window in O(N^3) time
# Time Coplexicity = O(N^3) => Result = TLE
# Space Complexity = O(1)
