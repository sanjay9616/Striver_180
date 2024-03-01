# Approach 1: Recursive Backtracking

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def recurPermute(index, nums, ans):
            if index == len(nums):
                ans.append(nums[:])
                return
            for i in range(index, len(nums)):
                nums[index], nums[i] = nums[i], nums[index]
                recurPermute(index + 1, nums, ans)
                nums[index], nums[i] = nums[i], nums[index]

        ans = []
        recurPermute(0, nums, ans)
        return ans

# Time Coplexicity = O(N * N!) => Result = Success (find all permutation + swap of n numbers)
# Space Complexity = O(N) // height of tree
