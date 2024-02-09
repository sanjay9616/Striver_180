# Approach 4: Using HasMap
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res = []
        hasMap, n = {}, len(nums)
        if (n == 1 or n == 2):
            return list(set(nums))
        for i in nums:
            if (i not in hasMap):
                hasMap[i] = 1
            else:
                hasMap[i] += 1
        for i in hasMap:
            if (hasMap[i] > n//3 and i not in res):
                res.append(i)
        return res


# Using Binary Search
# Time Coplexicity = (N) = O(N) => Result = Success
# Space Complexity = O(N)
