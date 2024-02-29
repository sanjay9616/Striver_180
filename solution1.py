# Approach 1: Brute Force

def minimumPlatform(self, n, arr, dep):
    plat_needed = 1
    result = 1
    for i in range(n):
        plat_needed = 1
        for j in range(n):
            if i != j:
                if (arr[i] >= arr[j] and dep[j] >= arr[i]):
                    plat_needed += 1
        result = max(result, plat_needed)
    return result

# Time Coplexicity = O(N^2) => Result = TLE
# Space Complexity = O(1)
