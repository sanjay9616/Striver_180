# Approach 2: Precalculation
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left, right = [0]*n, [0]*n
        res = 0
        left[0] = height[0]
        for i in range(1, n):
            left[i] = max(left[i-1], height[i])
        right[n-1] = height[n-1]
        for i in range(n-2, -1, -1):
            right[i] = max(right[i + 1], height[i])
        for i in range(n):
            res = res + min(left[i], right[i]) - height[i]
        return res

# Time Coplexicity = O(N) => Result = Success
# Space Complexity = O(N)
