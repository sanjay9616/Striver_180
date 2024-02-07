# Approach 1: Brute Force Approach using Linear Search
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if (matrix[i][j] == target):
                    return True
        return False


# Brute Force Approach using Linear Search
# Time Coplexicity = (m*n) = O(m*n) => Result = Success
# Space Complexity = O(1)
