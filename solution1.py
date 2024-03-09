# Approach 1: Brute Force
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        for i in range(len(nums) - k + 1):
            res.append(max(nums[i:i+k]))
        return res

# Time Coplexicity = O(N * k) => Result = TLE
# Space Complexity = O(1)
