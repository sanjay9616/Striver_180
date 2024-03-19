# Approach 1: Using Inorder
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        def inorder(root):
            if(not root):
                return []
            return inorder(root.left) + [root.val] + inorder(root.right)
        arr = inorder(root)
        n = len(arr)
        i, j = 0, n - 1
        while(i < j):
            currSum = arr[i] + arr[j]
            if(currSum < k):
                i +=1
            elif(currSum == k):
                return True
            else:
                j -= 1
        return False

# Time Coplexicity = O(N) => Result = Success
# Space Complexity = O(N) => height of the tree
