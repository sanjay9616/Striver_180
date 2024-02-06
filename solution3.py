# Approach 1: First sort Array and then compare adjucent
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums)-1):
            if (nums[i] == nums[i+1]):
                return nums[i]


# Transpose then Reverse individual rows
# Time Coplexicity = (n * log(n)) = O(n * log(n)) => Result = Success
# Space Complexity = O(1)
