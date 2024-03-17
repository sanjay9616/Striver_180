# Approach 1: Using Recursion (DFS) ## Solve Again
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if(not nums):
            return None
        mid = len(nums)//2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid + 1:])
        return root

# Time Coplexicity = O(N) => Result = Success
# Space Complexity = O(h)
