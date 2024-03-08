# Approach 1: Using Stack

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res, hasMap, stack = [], {}, [nums2[0]]
        for i in range(1, len(nums2)):
            while (stack and nums2[i] > stack[-1]):
                hasMap[stack[-1]] = nums2[i]
                stack.pop()
            stack.append(nums2[i])
        for i in stack:
            hasMap[i] = -1
        for i in nums1:
            res.append(hasMap[i])
        return res

# Time Coplexicity = O(N^2) => Result = Success
# Space Complexity = O(1)
