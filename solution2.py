# Approach 1: Binary Search  ## NEED TO REVISE

def median(matrix: [[int]], m: int, n: int) -> int:
    def count_smaller_than_mid(A, mid, n):
        l, h = 0, n - 1
        while (l <= h):
            md = (l + h) // 2
            if (A[md] <= mid):
                l = md + 1
            else:
                h = md - 1
        return l
    low, high = 1, 1000000000
    while (low <= high):
        mid = (low + high) // 2
        cnt = 0
        for i in range(m):
            cnt += count_smaller_than_mid(matrix[i], mid, n)
        if (cnt <= (n * m) // 2):
            low = mid + 1
        else:
            high = mid - 1
    return low

# Time Coplexicity =  O(M * lon(N)) => Result = Partially Accepted
# Space Complexity = O(1)
