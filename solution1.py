# Approach 1: Brute Force
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums[:] = sorted(set(nums))
        return len(nums)

# Time Coplexicity = O(N * log(N)) => Result = TLE
# Space Complexity = O(1)
