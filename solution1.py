# Approach 1: Brute Force Approach
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res, n = [], len(nums)
        if (n == 1 or n == 2):
            return list(set(nums))
        for i in range(n):
            c = 1
            for j in range(i+1, n):
                if (nums[i] == nums[j]):
                    c += 1
                    if (c > n//3):
                        res.append(nums[i])
                        break
        return list(set(res))


# Brute Force Approach
# Time Coplexicity = (n*n) = O(n^2) => Result = TLE
# Space Complexity = O(1)
