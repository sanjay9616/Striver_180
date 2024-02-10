# Approach 1: Brute Force Approach Usign Recursion
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if(m==1 or n==1):
            return 1
        return self.uniquePaths(m-1, n) + self.uniquePaths(m, n-1)


# Brute Force Approach Using Recursion
# Time Coplexicity = O(2^N) => Result = TLE
# Space Complexity = O(N+M)
