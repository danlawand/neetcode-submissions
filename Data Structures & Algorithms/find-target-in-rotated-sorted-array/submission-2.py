class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        n = len(nums)
        left = 0
        right = n-1
        while left < right:
            mid = (right + left)//2
            if nums[mid] > nums[right]:
                left = mid+1
            else:
                right = mid
        pivot = left

        def binarySearch(left, right):
            while left <= right:
                mid = (right + left)//2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    left = mid+1
                else:
                    right = mid-1
            return -1
        result = binarySearch(0, pivot-1)
        if result != -1:
            return result
        
        return binarySearch(pivot, n-1)

