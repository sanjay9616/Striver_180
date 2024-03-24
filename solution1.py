# Approach 1: Using Dynamic Programming
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1 for i in range(n)]
        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)
        return max(dp)

# Time Coplexicity = O(N^2) => Result = TLE
# Space Complexity = O(N)
