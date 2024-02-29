# Approach 1: Brute Force

class Solution:
    def fractionalknapsack(self, W, arr, n):
        arr.sort(key=lambda x: x.value/x.weight, reverse=True)
        res = 0
        for i in arr:
            if (W >= i.weight):
                res += i.value
                W -= i.weight
            else:
                res += i.value / i.weight * W
                break
        return res

# Time Coplexicity = O(N * log(N)) => Result = Success
# Space Complexity = O(1)
