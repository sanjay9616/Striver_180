# Approach 1: Brute Force

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return sorted(nums, reverse=True)[k-1]

# Time Coplexicity = O(N * log(N)) => Result = Success
# Space Complexity = O(1)
