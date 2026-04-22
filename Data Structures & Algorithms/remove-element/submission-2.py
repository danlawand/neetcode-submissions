class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        l = 0
        r = n-1
        while l <= r:
            if nums[r] == val:
                r -= 1
                continue
            if nums[l] == val:
                nums[l], nums[r] = nums[r], nums[l]
                r -= 1
            l += 1
        return l

    def _removeElement(self, nums: List[int], val: int) -> int:
        maxNum = 101
        n = len(nums)
        removed = 0

        for i in range(n):
            if nums[i] == val:
                nums[i] = maxNum
                removed += 1
        
        nums.sort()
        return n-removed
        
        