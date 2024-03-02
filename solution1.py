# Approach 1: Brute Force

def median(matrix: [[int]], m: int, n: int) -> int:
    l = []
    for i in range(m):
        for j in range(n):
            l.append(matrix[i][j])
    l.sort()
    mid = len(l) // 2
    if (len(l) % 2 == 0):
        median = (l[mid-1] + l[mid]) / 2
    else:
        median = l[mid]
    return median

# Time Coplexicity = O((M * N) + (M + N) * log(M + N)) = O((M + N) * log(M + N)) => Result = Partially Accepted
# Space Complexity = O(M + N)
