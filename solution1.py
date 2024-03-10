# Approach 1: Briute Force (One Line)

class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(s.split()[::-1])


# Time Coplexicity = O(N) => Result = TLE
# Space Complexity = O(N)
