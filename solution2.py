# Approach 2: Using Sorting
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

# Time Coplexicity = O(N * log(N)) => Result = Success
# Space Complexity = O(1)
