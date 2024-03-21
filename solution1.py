# Approach 1: Brute Force

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums

    def add(self, val: int) -> int:
        self.nums.append(val)
        return sorted(self.nums)[len(self.nums) - self.k]

# Time Coplexicity = O(N * log(N)) => Result = TLE
# Space Complexity = O(1)