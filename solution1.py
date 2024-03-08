# Approach 1: Brute Force
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        for i in range(len(nums1)):
            inx = -1
            for j in range(len(nums2)):
                if (nums1[i] == nums2[j]):
                    inx = j
                    break
            for j in range(inx, len(nums2)):
                flag = False
                if (nums2[j] > nums1[i]):
                    flag = True
                    res.append(nums2[j])
                    break
            if (not flag):
                res.append(-1)
        return res

# Time Coplexicity = O(N^2) => Result = Success
# Space Complexity = O(1)