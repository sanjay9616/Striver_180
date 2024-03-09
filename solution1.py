# Approach 1: Brute Force
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = float('-inf')
        for i in range(len(heights)):
            minHeight = float('inf')
            for j in range(i, len(heights)):
                minHeight = min(minHeight, heights[j])
                res = max(res, minHeight * (j - i + 1))
        return res

# Time Coplexicity = O(N^2) => Result = TLE
# Space Complexity = O(1)
