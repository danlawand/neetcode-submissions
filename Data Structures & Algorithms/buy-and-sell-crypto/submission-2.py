class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        n = len(prices)
        for i in range(n):
            for j in range(i+1, n):
                maxProfit = max(maxProfit, prices[j]-prices[i])
        return maxProfit