class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit, buy = 0, prices[0]
        for i in range(len(prices)):
            if (buy > prices[i]):
                buy = prices[i]
            elif (prices[i] - buy > maxProfit):
                maxProfit = prices[i] - buy
        return maxProfit

# Greedy Approach
# Time Coplexicity = (n) = O(n) => Result = Success
# Space Complexity = O(1)