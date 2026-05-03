class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n <= 0:
            return 0
        maxProfit = 0
        for i in range(n):
            for j in range(i+1, n):
                maxProfit = max(maxProfit, prices[j]-prices[i])
        return maxProfit