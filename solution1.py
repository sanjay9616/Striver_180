# Approach 1: Brute Force Approach using Linear Search
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            c = 0
            for j in range(i+1, len(nums)):
                if (nums[i] == nums[j]):
                    return nums[i]


# Brute Force Approach using Linear Search
# Time Coplexicity = (n*n) = O(n^2) => Result = TLE
# Space Complexity = O(1)
