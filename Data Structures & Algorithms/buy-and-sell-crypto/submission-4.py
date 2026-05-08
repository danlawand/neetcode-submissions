class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        for i, price in enumerate(prices):
            for j in range(i+1, len(prices)):
                maxProfit = max(maxProfit, prices[j]-price)
        return maxProfit