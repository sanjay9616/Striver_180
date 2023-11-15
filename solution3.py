def setZeroes(matrix):
    n, m = len(matrix[0]), len(matrix)
    col0 = 1
    for i in range(m):
        for j in range(n):
            if (matrix[i][j] == 0):
                matrix[i][0] = 0
                if (j != 0):
                    matrix[0][j] = 0
                else:
                    col0 = 0
    for i in range(1, m):
        for j in range(1, n):
            if (matrix[i][0] == 0 or matrix[0][j] == 0):
                matrix[i][j] = 0
    if (matrix[0][0] == 0):
        for i in range(n):
            matrix[0][i] = 0
    if (col0 == 0):
        for i in range(m):
            matrix[i][0] = 0

    return matrix


print(setZeroes([[1, 1, 1], [1, 0, 1], [1, 1, 1]]))
# Output = [[1, 0, 1], [0, 0, 0], [1, 0, 1]]

print(setZeroes([[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]))
# Output = [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]


# Optimal Solution
# Time Coplexicity = ( m * n ) + ( m * n ) = O(n2) => Result = Accepted
# Space Complexity = O(1) - using extra space
