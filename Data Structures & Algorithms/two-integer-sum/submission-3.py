class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numberMapper = {}
        for idx, number in enumerate(nums):
            if target-number in numberMapper:
                return [numberMapper[target-number], idx]
            numberMapper[number] = idx
        return [-1,-1]