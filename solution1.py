# Approach 1: Brute Force
def subarraysWithSumK(a: [int], b: int) -> int:
    # Write your code here
    n = len(a)
    res = 0
    for i in range(n):
        xor = 0
        for j in range(i, n):
            xor = xor ^ a[j]
            if(xor == b):
                res += 1
    return res

    pass



# Brute Force
# Time Coplexicity = O(N^2) => Result = TLE
# Space Complexity = O(1)
