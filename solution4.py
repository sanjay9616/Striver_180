# Approach 4: Using Moore’s Voting Algorithm
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if (n == 1 or n == 2):
            return list(set(nums))
        element1, element2 = None, None
        count1, count2 = 0, 0
        for i in range(n):
            if (count1 == 0 and nums[i] != element2):
                element1 = nums[i]
                count1 = 1
            elif (count2 == 0 and nums[i] != element1):
                element2 = nums[i]
                count2 = 1
            elif (element1 == nums[i]):
                count1 += 1
            elif (element2 == nums[i]):
                count2 += 1
            else:
                count1 -= 1
                count2 -= 1
        count1 = 0
        count2 = 0
        res = []
        for i in range(n):
            if (element1 == nums[i]):
                count1 += 1
        for i in range(n):
            if (element2 == nums[i]):
                count2 += 1
        if (count1 > n//3):
            res.append(element1)
        if (count2 > n//3):
            res.append(element2)
        return res


# Using Moore’s Voting Algorithm
# Time Coplexicity = O(N) => Result = Success
# Space Complexity = O(1)
