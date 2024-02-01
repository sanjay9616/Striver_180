class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        from itertools import combinations
        for p in combinations(prices, 2):
            maxProfit = max(maxProfit, p[1]-p[0])
        return maxProfit


# Brute Force - Using python functions
# Time Coplexicity = (n * n) = O(n^2) => Result = TLE
# Space Complexity = O(1)
