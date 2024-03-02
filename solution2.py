# Approach 2: Using XOR
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        xor = 0
        for i in nums:
            xor ^= i
        return xor

# Time Coplexicity =  O(N) => Result = Success
# Space Complexity = O(1)
