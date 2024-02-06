# Approach 1: Using HasMap
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hasMap = {}
        for i in nums:
            if (i not in hasMap):
                hasMap[i] = 1
            else:
                hasMap[i] += 1
        for i in hasMap:
            if (hasMap[i] >= 2):
                return i


# Using HasMap
# Time Coplexicity = (n)) = O(n) => Result = Success
# Space Complexity = O(N)
