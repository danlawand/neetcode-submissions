class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeft = 0
        maxRight = 0
        left = 0
        right = len(height)-1
        maxArea = 0
        while left <= right:
            maxRight = max(maxRight, height[right])
            maxLeft = max(maxLeft, height[left])
            if height[left] < height[right]:
                currArea = min(maxLeft, maxRight) - height[left]
                if currArea > 0:
                    maxArea += currArea
                left += 1
            else:
                currArea = min(maxLeft, maxRight) - height[right]
                if currArea > 0:
                    maxArea += currArea
                right -= 1
        return maxArea
                
    # Time O(n)
    # AUx mem O(n)
    def _trap(self, height: List[int]) -> int:
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
