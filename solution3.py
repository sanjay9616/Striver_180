# Approach 2: Using Binary Search
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        low, high = 0, m * n - 1
        while (low <= high):
            mid = (low + high) // 2
            row = mid // 2
            col = mid % 2
            if (matrix[row][col] == target):
                return True
            elif (matrix[row][col] < target):
                high = mid - 1
            elif (matrix[row][col] > target):
                high = mid + 1
        return False

# Flatten 2d into 1d -> apply Binary Search
# Time Coplexicity = (log(m*n)) = O(log(m*n)) => Result = Success
# Space Complexity = O(1)
