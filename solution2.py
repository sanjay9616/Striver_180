### Approach 1: Transpose then Reverse individual rows
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)

        def Transpose(matrix): # Only Works on Square matrix n * n
            for i in range(n):
                for j in range(i+1, n):
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            return matrix

        def reverseEachRow(matrix):
            for i in range(n):
                for j in range(n//2):
                    matrix[i][j], matrix[i][n- 1 - j] = matrix[i][n - 1 - j], matrix[i][j]
        reverseEachRow(Transpose(matrix))


# Transpose then Reverse individual rows
# Time Coplexicity = (n * n) = O(n^2) => Result = Success
# Space Complexity = O(1)
