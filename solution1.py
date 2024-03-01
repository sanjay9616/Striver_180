# Approach 1: Recursive Approach

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        if not s:
            return [[]]
        ans = []
        for i in range(1, len(s) + 1):
            if s[:i] == s[:i][::-1]:
                for suf in self.partition(s[i:]):
                    ans.append([s[:i]] + suf)
        return ans

# Time Coplexicity = O(N * 2^N) => Result = Success
# Space Complexity = O(N)
