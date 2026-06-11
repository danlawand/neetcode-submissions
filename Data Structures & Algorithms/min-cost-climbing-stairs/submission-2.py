class Solution:
    # Time O(2^n)
    # Space O(n) because the recursive calls are not all active 
    #   simultaneously.
    #   Once a branch returns, its stack frames are removed.
    def _minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        return min(self.recursiveMinCostClimbingStairs(0, cost), self.recursiveMinCostClimbingStairs(1, cost))
    
    def recursiveMinCostClimbingStairs(self, ith: int, cost: List[int]) -> int:
        if ith >= len(cost):
            return 0
        if ith == len(cost)-1:
            return cost[ith]
        
        return cost[ith] + min(self.recursiveMinCostClimbingStairs(ith+1, cost), self.recursiveMinCostClimbingStairs(ith+2, cost))

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        if n <= 0:
            return -1
        if n == 1:
            return cost[0]
        if n == 2:
            return min(cost[0], cost[1])

        aggregatedCost = [0]*(n+1)
        aggregatedCost[1] = cost[0]
        aggregatedCost[2] = cost[1]
        for i in range(3, n+1):
            aggregatedCost[i] = cost[i-1] + min(aggregatedCost[i-1], aggregatedCost[i-2])
        return min(aggregatedCost[n], aggregatedCost[n-1])
