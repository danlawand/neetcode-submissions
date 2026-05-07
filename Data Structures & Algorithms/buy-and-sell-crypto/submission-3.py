class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        n = len(prices)
        buyDay = 0
        for sellDay in range(n):
            if prices[sellDay] < prices[buyDay]:
                buyDay = sellDay
            else:
                maxProfit = max(maxProfit, prices[sellDay]-prices[buyDay])
        return maxProfit