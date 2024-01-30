class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        M=float('-inf')
        for i in range(len(nums)):
            s=0
            for j in range(i,len(nums)):
                s+=nums[j]
                M=max(M,s)
        return M


# Brute Force Algorithm
# Time Coplexicity = (n*n) = O(n^2) => Result = Time Limit Exceeded
# Space Complexity = O(1)
