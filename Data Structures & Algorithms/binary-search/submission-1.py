class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.recBinarySearch(0, len(nums)-1, nums, target)
    def recBinarySearch(self, left, right, nums, target):
        if left > right:
            return -1
        mid = left + (right-left)//2
        if nums[mid] == target:
            return mid
        if nums[mid] > target:
            return self.recBinarySearch(left, mid-1, nums, target)
        return self.recBinarySearch(mid+1, right, nums, target)
    def _search(self, nums: List[int], target: int) -> int:
        right = len(nums)-1
        left = 0
        while left <= right:
            mid = left + (right-left)//2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                right = mid-1
            else:
                left = mid+1
        return -1
        