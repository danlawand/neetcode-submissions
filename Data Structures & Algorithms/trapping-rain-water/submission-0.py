class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        maxLeft = height[0]
        leftHighestBar = [0 for _ in range(n)]
        for i in range(1, n):
            maxLeft = max(maxLeft, height[i])
            leftHighestBar[i] = maxLeft

        rightHighestBar = [0 for _ in range(n)]
        maxRight = height[-1]
        for i in range(n-2, -1, -1):
            maxRight = max(maxRight, height[i])
            rightHighestBar[i] = maxRight
        

        maxArea = 0
        for i in range(n):
            currArea = min(rightHighestBar[i], leftHighestBar[i]) - height[i]
            if currArea > 0:
                maxArea += currArea
        return maxArea
