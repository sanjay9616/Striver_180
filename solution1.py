# Approach 1: Brute Force Approach using Linear Search
class Solution:
    # @param A : tuple of integers
    # @return a list of integers
    def repeatedNumber(self, A):
        l = []
        for i in range(len(A)):
            for j in range(i+1, len(A)):
                if (A[i] == A[j]):
                    l.append(A[i])
        for i in range(1, len(A)):
            found = False
            temp = i
            for j in range(len(A)):
                if (i == A[j]):
                    found = True
                    temp = i
                    break
            if (not found):
                l.append(temp)
                break
        return l


# Brute Force Approach using Linear Search
# Time Coplexicity = (n*n) = O(n^2) => Result = TLE
# Space Complexity = O(1)
