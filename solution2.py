# Approach 2: Brute Force (using python function itertools)

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        from itertools import combinations
        res, n = [], len(nums)
        for p in combinations(nums, 3):
            if sum(p) == 0:
                if len(res) > 0:
                    count = 0
                    for result in res:
                        if sorted(result) != sorted([p[0], p[1], p[2]]):
                            count += 1
                    if count == len(res):
                        res.append([p[0], p[1], p[2]])
                else:
                    res.append([p[0], p[1], p[2]])
        return res

###############           OR               ###################


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        from itertools import combinations
        res, n = [], len(nums)
        for p in combinations(nums, 3):
            if (sum(p) == 0):
                if (sorted(list(p)) not in res):
                    res.append(sorted(list(p)))
        return res

# Time Coplexicity = O(N^4 * log(N)) => Result = TLE
# Space Complexity = O(1)
