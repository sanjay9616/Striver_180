# Approach 1: Using HasMap
class Solution:
    # @param A : tuple of integers
    # @return a list of integers
    def repeatedNumber(self, A):
        hasMap = {}
        for i in A:
            if (i not in hasMap):
                hasMap[i] = 1
            else:
                hasMap[i] += 1
        l = [0, 0]
        for i in range(1, len(A)+1):
            if (i not in hasMap):
                l[1] = i
            elif (hasMap[i] >= 2):
                l[0] = i
        return l


# Using HasMap
# Time Coplexicity = (n)) = O(n) => Result = Success
# Space Complexity = O(N)
