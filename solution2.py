# Approach 1: Using Stack

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        # left boundary => next smaller element to left
        stack = []
        leftSmaller = [0]*n
        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                leftSmaller[i] = stack[-1] + 1
            stack.append(i)
        # right boundary => next smaller element to right
        stack = []
        rightSmaler = [n-1]*n
        for i in range(n-1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                rightSmaler[i] = stack[-1] - 1
            stack.append(i)
        res = heights[0]
        for i in range(n):
            res = max(res, (rightSmaler[i] - leftSmaller[i] + 1) * heights[i])
        return res

# Time Coplexicity = O(N + N + N) = O(N) => Result = Success
# Space Complexity = O(N + N + N) = O(N)
