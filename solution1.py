# Approach 1: Brute Force

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l = sorted(nums1 + nums2)
        if (len(l) % 2 == 1):
            return l[len(l) // 2]
        else:
            return (l[len(l) // 2 - 1] + l[len(l) // 2]) / 2

# Time Coplexicity = O((N + M) * log(N + M)) => Result = Success
# Space Complexity = O(N + M)
