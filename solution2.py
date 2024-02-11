# Approach 2: Brute Force
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        res = 0
        c = 0
        for i in range(len(nums)):
            if(i==0):
                c += 1
                res = max(res, c)
                continue
            elif(nums[i] == nums[i-1]):
                res = max(res, c)
                continue
            elif(nums[i] - 1 == nums[i-1]):
                c += 1
            else:
                c = 1
            res = max(res, c)
        return res

# Better Approach
# Time Coplexicity = O(N * log(N)) => Result = Success
# Space Complexity = O(1)