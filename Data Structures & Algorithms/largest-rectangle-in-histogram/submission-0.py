class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        maxArea = -1
        for i in range(n):
            currMinHeight = heights[i]
            currMaxArea = heights[i]
            for j in range(i+1, n):
                if currMinHeight > heights[j]:
                    currMinHeight = heights[j]
                currMaxArea = max(currMaxArea, currMinHeight*(j-i+1))
            maxArea = max(maxArea, currMaxArea)
        return maxArea