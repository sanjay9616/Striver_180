# Approach 1: Using Traversal From Starting and End of an Array

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        prefix, suffix, n = 1, 1, len(nums)
        res = max(nums)
        for i in range(n):
            if (prefix == 0):
                prefix = 1
            if (suffix == 0):
                suffix = 1
            prefix *= nums[i]
            suffix *= nums[n - i - 1]
            res = max(res, suffix, prefix)
        return res

# Time Coplexicity = O(N) => Result = Success
# Space Complexity = O(1)
