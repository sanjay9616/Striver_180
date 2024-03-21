# Approach 1: Brute Force

def countDistinctElements(arr, k):
    res = []
    for i in range(len(arr) - k + 1):
        res.append(len(set(arr[i:i+k])))
    return res

# Time Coplexicity = O(N^2) => Result = Success
# Space Complexity = O(1)
