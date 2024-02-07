# Approach 2: Using Binary Search
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binarySearch(arr, x):
            l, r = 0, len(arr) - 1
            while l <= r:
                mid = l + (r - l) // 2
                if arr[mid] == x:
                    return True
                elif arr[mid] < x:
                    l = mid + 1
                else:
                    r = mid - 1
            return False
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            if (matrix[i][0] <= target and target <= matrix[i][n - 1]):
                return binarySearch(matrix[i], target)

# Using Binary Search
# Time Coplexicity = (m + log(n)) = O(m*n) => Result = Success
# Space Complexity = O(1)
