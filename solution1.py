# Approach 1: Brute Force
class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        c =0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if(nums[i] > nums[j]*2):
                    c += 1
        return c
        

# Brute Force Approach Using Recursion
# Time Coplexicity = O(N^2) => Result = TLE
# Space Complexity = O(1)
