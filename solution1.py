# Approach 1: By Sorting

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        first = strs[0]
        last = strs[-1]
        res = ""
        for i in range(min(len(first), len(last))):
            if(first[i] != last[i]):
                return res
            res += first[i]
        return res

# Time Coplexicity = O(N * log(N)) => Result = Success
# Space Complexity = O(1)
