# Approach 2: Optimized
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        replace = 1
        for i in range(1, len(nums)):
            if nums[i-1] != nums[i]:
                nums[replace] = nums[i]
                replace += 1
        return replace

# Time Coplexicity = O(N) => Result = Success
# Space Complexity = O(1)
