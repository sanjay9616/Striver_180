# Approach 1: Linear Search

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if(nums[i]==target):
                return i
        return -1

# Time Coplexicity = O(N) => Result = Success
# Space Complexity = O(1)
