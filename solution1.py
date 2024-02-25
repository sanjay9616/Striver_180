# Approach 1: Brute Force
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res, count = 0, 0
        for i in nums:
            if(i == 0):
                count = 0
            else:
                count += 1
                res = max(res, count)
        return res

# Time Coplexicity = O(N) => Result = Success
# Space Complexity = O(1)
