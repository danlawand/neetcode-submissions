class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights)-1
        maxArea = 0
        while left < right:
            currArea = min(heights[left], heights[right])*(right-left)
            maxArea = max(maxArea, currArea)
            if heights[left] <= heights[right]:
                left += 1
            else:
                right -= 1
        return maxArea
    def _maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        maxArea = 0
        for i in range(n):
            for j in range(i+1, n):
                currArea = min(heights[i], heights[j])*(j-i)
                maxArea = max(maxArea, currArea)
        return maxArea