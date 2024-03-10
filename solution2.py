# Approach 2: Dynamic Programming  ## NEED TO SEE VIDEO

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        maxLength=1
        res=s[0]
        dp = [[False for _ in range(len(s))] for _ in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = True
            for j in range(i):
                if s[j] == s[i] and (i == j + 1 or dp[j+1][i-1]):
                    dp[j][i] = True
                    if i-j+1 > maxLength:
                        maxLength = i-j+1
                        res = s[j:i+1]
        return res

# Time Coplexicity = O(N^2) => Result = Success
# Space Complexity = O(N^2)