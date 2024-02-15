# Approach 1: Using Sliding Window in O(N^2) time

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            visited = [False]*256
            for j in range(i, len(s)):
                if(visited[ord(s[j])]):
                    break
                else:
                    visited[ord(s[j])] = True
                    res = max(res, j - i + 1)
            # visited[ord(s[i])] = True
        return res

# Using Sliding Window in O(N^2) time
# Time Coplexicity = O(N^2) => Result = Success
# Space Complexity = O(1)
