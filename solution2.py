# Approach 2: Using Sort
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l1 = []
        for i in range(len(nums)):
            l1.append([nums[i], i])
        l1.sort()
        i, j = 0, len(nums)-1
        while(i<j):
            sum = l1[i][0]+l1[j][0]
            if(sum == target):
                return [l1[i][1], l1[j][1]]
            if(target > sum):
                i += 1
            else:
                j -= 1

# Using Sort
# Time Coplexicity = O(N * log(N)) => Result = Success
# Space Complexity = O(N)
