class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numCounter = {}
        for num in nums:
            if num in numCounter:
                numCounter[num] += 1
            else:
                numCounter[num] = 1
            if numCounter[num] >= 2:
                return True
        return False
