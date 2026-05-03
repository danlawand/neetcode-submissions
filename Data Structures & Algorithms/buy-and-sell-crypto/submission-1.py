class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n <= 0:
            return 0
        maxProfit = 0
        p1 = 0
        p2 = 1
        while p2 < n:
            if prices[p1] > prices[p2]:
                p1 = p2
            else:
                maxProfit = max(maxProfit, prices[p2]-prices[p1])
            p2 += 1

        return maxProfit
