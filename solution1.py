class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero, one, two = 0, 0, 0
        for i in nums:
            if (i == 0):
                zero += 1
            elif (i == 1):
                one += 1
            elif (i == 2):
                two += 1
        i = 0
        while (zero > 0):
            nums[i] = 0
            i += 1
            zero -= 1
        while (one > 0):
            nums[i] = 1
            i += 1
            one -= 1
        while (two > 0):
            nums[i] = 2
            i += 1
            two -= 1


# The basic idea that comes to mind is to simply count the number of 0’s, 1’s, and 2’s. Then, place all 0’s at the beginning of the array followed by 1’s and 2's.
# Time Coplexicity = (n + n) = O(2n) => Result = Success
# Space Complexity = O(1)
