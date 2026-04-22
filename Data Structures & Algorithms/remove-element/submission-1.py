class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        maxNum = 101
        n = len(nums)
        removed = 0

        for i in range(n):
            if nums[i] == val:
                nums[i] = maxNum
                removed += 1
        
        nums.sort()
        return n-removed
        
        