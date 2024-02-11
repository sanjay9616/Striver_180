# Approach 1: Brute Force
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)):
            nextElement = nums[i]+1
            c = 1
            while(nextElement in nums):
                c += 1
                nextElement += 1
            res = max(res, c)
        return res


# Brute Force
# Time Coplexicity = O(N^2) => Result = TLE
# Space Complexity = O(1)
