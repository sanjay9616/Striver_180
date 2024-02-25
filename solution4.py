# Approach 4: Horizontal Scan Method
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        totalBlock = sum(height)
        maxHeight = max(height)
        res = 0
        left, right = 0, n-1
        for i in range(1, maxHeight+1):
            while (height[left] < i):
                left += 1
            while (height[right] < i):
                right -= 1
            res += (right - left + 1)
        res -= totalBlock
        return res

# Time Coplexicity = O(max(max_height, N)) => Result = Success
# Space Complexity = O(1)
