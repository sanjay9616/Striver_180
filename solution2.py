def setZeroes(matrix):
    n, m = len(matrix[0]), len(matrix)
    row, col = [0]*m, [0]*n
    for i in range(m):
        for j in range(n):
            if (matrix[i][j] == 0):
                row[i] = col[j] = 1
    for i in range(m):
        for j in range(n):
            if (row[i] == 1 or col[j] == 1):
                matrix[i][j] = 0

    return matrix


print(setZeroes([[1, 1, 1], [1, 0, 1], [1, 1, 1]]))
# Output = [[1, 0, 1], [0, 0, 0], [1, 0, 1]]

print(setZeroes([[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]))
# Output = [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]


# Better then Brute Force Algorithm
# Time Coplexicity = ( m * n ) + ( m * n ) = O(n2) => Result = Accepted
# Space Complexity = O(M) + O(N) - using extra space
