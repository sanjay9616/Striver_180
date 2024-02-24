# Approach 1: Brute Force
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res, n = [], len(nums)
        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    if (nums[i]+nums[j]+nums[k] == 0):
                        if (len(res) > 0):
                            count = 0
                            for result in res:
                                if (sorted(result) != sorted([nums[i], nums[j], nums[k]])):
                                    count += 1
                            if (count == len(res)):
                                res.append([nums[i], nums[j], nums[k]])
                        else:
                            res.append([nums[i], nums[j], nums[k]])
        return res


# Time Coplexicity = O(N^log(N)) => Result = TLE
# Space Complexity = O(1)
