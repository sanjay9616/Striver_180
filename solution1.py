# Approach 1: Brute Force
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        for i in range(len(nums)):
            mul = nums[i]
            for j in range(i + 1, len(nums)):
                mul = mul * nums[j]
                res = max(res, mul)
        return res

# Time Coplexicity = O(N^2) => Result = TLE
# Space Complexity = O(1)
