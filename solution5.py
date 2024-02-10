# Approach 4: Using DP (Space Optimization)
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # calculate = (m + n-2)! / (n-1)! (m-1)!
        v1, v2, v3 = 1, 1, 1
        for i in range(m+n-2, 0, -1):
            v1 *= i
        for i in range(n-1, 0, -1):
            v2 *= i
        for i in range(m-1, 0, -1):
            v3 *= i
        return v1//(v2*v3)

#        OR      #

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # calculate = (m + n-2)! / (n-1)! (m-1)!
        path = 1
        for i in range(n, (m + n - 1)):
            path *= i
            path //= (i - n + 1)
        return path

# Using DP (Space Optimization)
# Time Coplexicity = O(M) => Result = Success
# Space Complexity = O(1)