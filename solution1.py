def setZeroes(matrix):
    n, m = len(matrix[0]), len(matrix)
    for i in range(m):
        for j in range(n):
            if (matrix[i][j] == 0):
                for row in range(0, m):
                    if (matrix[row][j] != 0):
                        matrix[row][j] = -1
                for col in range(0, n):
                    if (matrix[i][col] != 0):
                        matrix[i][col] = -1
    for i in range(m):
        for j in range(n):
            if (matrix[i][j] == -1):
                matrix[i][j] = 0
    return matrix


print(setZeroes([[1, 1, 1], [1, 0, 1], [1, 1, 1]]))
# Output = [[1, 0, 1], [0, 0, 0], [1, 0, 1]]

print(setZeroes([[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]))
# Output = [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]

# Brute Force Algorithm
# Time Coplexicity = ( m * n ) * ( m + n ) + ( m * n ) = O(n3) => Result = Time Limit Exceeded
# Space Complexity = O(1)
