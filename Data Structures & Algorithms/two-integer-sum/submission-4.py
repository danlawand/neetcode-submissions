class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        twoSumDict = {}
        for idx, num in enumerate(nums):
            if target-num in twoSumDict:
                return [twoSumDict[target-num], idx]
            twoSumDict[num] = idx

        return [-1,-1]
