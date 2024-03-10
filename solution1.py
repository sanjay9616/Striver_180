# Approach 1: Brute Force

class Solution:
    def solve(self, A):
        res = 0
        while (len(A) > 0):
            if (A == A[::-1]):
                return res
            A = A[:-1]
            res += 1
        return res

# Time Coplexicity = O(N^2) => Result = TLE
# Space Complexity = O(1)
