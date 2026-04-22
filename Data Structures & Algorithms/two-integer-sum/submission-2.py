class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        numberCounter = {}
        for i, number in enumerate(nums):
            if target-number in numberCounter:
                return [numberCounter[target-number], i]
            numberCounter[number] = i
        return [-1, -1]
