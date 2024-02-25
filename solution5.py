# Approach 5: Two Pointer ## Need To Revised

class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left, right = 0, n - 1
        l_max, r_max = 0, 0
        res = 0
        while (left <= right):
            if r_max <= l_max:
                res += max(0, r_max - height[right])
                r_max = max(r_max, height[right])
                right -= 1
            else:
                res += max(0, l_max - height[left])
                l_max = max(l_max, height[left])
                left += 1
        return res

# Time Coplexicity = O(N) => Result = Success
# Space Complexity = O(1)
