# Approach 2: Efficient Iterative Method

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for i in range(len(nums)):
            for j in range(len(res)):
                l = sorted([nums[i]] + res[j])
                if (l not in res):
                    res.append(l)
        return res

# Time Coplexicity = O(2^N * N) => Result = Success
# Space Complexity = O(1)
