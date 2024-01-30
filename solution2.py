class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = float('-inf')
        currSum = 0
        for i in range(0, len(nums)):
            currSum += nums[i]
            if(currSum > maxSum):
                maxSum = currSum
            if(currSum < 0):
                currSum = 0
        return maxSum

# Kadane’s Algorithm
# Time Coplexicity = (n) = O(n) => Result = Success
# Space Complexity = O(1)