# Approach 1: Brute Force

class Solution:
    def kthElement(self,  arr1, arr2, n, m, k):
        l = sorted(arr1 + arr2)
        return l[k - 1]

# Time Coplexicity = O((N + M) * log(N + M)) => Result = Success
# Space Complexity = O(N + M)
