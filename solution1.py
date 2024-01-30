class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        inx = -1
        for i in range(len(nums)-2, -1, -1):
            # print(i, i+1)
            if(nums[i] < nums[i+1]):
                inx = i
                break
        if(inx == -1):
            nums[:] = nums[:][::-1]
        else:
            m = nums[inx+1]
            mInx = inx+1
            for i in range(i+1, len(nums)):
                if(m >= nums[i] and nums[inx] < nums[i]):
                    m = nums[i]
                    mInx = i
            nums[inx], nums[mInx] = nums[mInx], nums[inx]
            nums[:] = nums[:inx+1]+nums[inx+1:][::-1]

[2, 3, 1, 3, 3] # OutPut - [2, 3, 3, 1, 3]


# Brute Force Algorithm
# Time Coplexicity = (3n) = O(n) => Result = Time Limit Exceeded
# Space Complexity = O(1)
