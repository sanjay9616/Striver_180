# Approach 4:  Using DP
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        res = [[0 for i in range(n)] for j in range(m)]
        for i in range(m):
            res[i][0] = 1
        for i in range(n):
            res[0][i] = 1
        for i in range(1, m):
            for j in range(1, n):
                res[i][j] = res[i-1][j] + res[i][j-1]
        return res[m-1][n-1]

#  Using DP
# Time Coplexicity = O(M * N) => Result = Success
# Space Complexity = O(M * N)
