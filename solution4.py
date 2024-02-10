# Approach 4: Using DP (Space Optimization)
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        res = [1 for i in range(n)]
        for i in range(m - 1):
            for j in range(1, n):
                res[j] += res[j - 1]
        return res[n - 1]

# Using DP (Space Optimization)
# Time Coplexicity = O(M * N) => Result = Success
# Space Complexity = O(N)
