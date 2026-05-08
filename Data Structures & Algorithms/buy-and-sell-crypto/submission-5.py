class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        n = len(prices)
        buyIdx = 0
        for sellIdx in range(n):
            if prices[sellIdx] <= prices[buyIdx]:
                buyIdx = sellIdx
            else:
                maxProfit = max(maxProfit, prices[sellIdx]-prices[buyIdx])
        return maxProfit