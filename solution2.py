# Approach 1: Using Two Pointer

class Solution:
    def solve(self, A):
        res = 0
        while (len(A) > 0):
            if (A == A[::-1]):
                return res
            A = A[:-1]
            res += 1
        return res

# Time Coplexicity = O(N) or o(N^2) => Result = TLE
# Space Complexity = O(1)
