def generate(numRows):
    if (numRows == 0):
            return []
    l = [[1]]
    for i in range(numRows-1):
        l.append([sum(i) for i in zip(l[-1]+[0], [0]+l[-1])])
    return l


print(generate(5))
# Output = [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

print(generate(1))
# Output = [[1]]

# Brute Force Algorithm
# Time Coplexicity = ( m * n ) * ( m + n ) + ( m * n ) = O(n3) => Result = Time Limit Exceeded
# Space Complexity = O(1)
