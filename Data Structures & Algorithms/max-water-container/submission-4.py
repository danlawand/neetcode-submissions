class Solution:
    def maxArea(self, h: List[int]) -> int:
        maxArea = 0
        left = 0
        right = len(h)-1

        while left <= right:
            currArea = min(h[left], h[right])*(right-left)
            maxArea = max(maxArea, currArea)
            if h[left] < h[right]:
                left += 1
            else:
                right -= 1
        return maxArea