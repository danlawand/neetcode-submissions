class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        maxArea = 0
        for i in range(n):
            for j in range(i+1, n):
                currArea = min(heights[i], heights[j])*(j-i)
                maxArea = max(maxArea, currArea)
        return maxArea