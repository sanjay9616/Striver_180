# Approach 2: Using HasMap
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hasMap = {}
        for i in range(len(nums)):
            if(target-nums[i] not in hasMap):
                hasMap[nums[i]] = i
            else:
                return [hasMap[target-nums[i]], i]

# Using HasMap
# Time Coplexicity = O(N) => Result = Success
# Space Complexity = O(N)