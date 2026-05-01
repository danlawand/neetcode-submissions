class Solution:
    def findMin(self, nums: List[int]) -> int:
        if not nums:
            return -1
        left = 0
        right = len(nums)-1
        minValue = nums[0]
        while left <= right:
            if nums[left] < nums[right]:
                return min(minValue, nums[left])
            mid = left + (right-left)//2
            minValue = min(minValue, nums[mid])
            if nums[mid] >= nums[left]:
                left = mid + 1
            else:
                right = mid-1
        return minValue