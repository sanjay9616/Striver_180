# Approach 2: Two Pointer
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1, n2 = len(nums1), len(nums2)
        i, j = 0, 0
        l = []
        while (i < n1 and j < n2):
            if (nums1[i] < nums2[j]):
                l.append(nums1[i])
                i += 1
            elif (nums1[i] == nums2[j]):
                l.append(nums1[i])
                l.append(nums2[j])
                i += 1
                j += 1
            else:
                l.append(nums2[j])
                j += 1
        while (i < n1):
            l.append(nums1[i])
            i += 1
        while (j < n2):
            l.append(nums2[j])
            j += 1
        if (len(l) % 2 == 1):
            return l[len(l) // 2]
        else:
            return (l[len(l) // 2 - 1] + l[len(l) // 2]) / 2

# Time Coplexicity =  O(N + M) => Result = Success
# Space Complexity = O(N + M)
