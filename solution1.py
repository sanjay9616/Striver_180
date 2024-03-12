# Approach 1: Brute Force
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        for i in set(s + t):
            if (s.count(i) != t.count(i)):
                return False
        return True

# Time Coplexicity = O(N^2) => Result = Success
# Space Complexity = O(N)
