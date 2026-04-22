class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        numberCounter = {}
        for n in nums:
            numberCounter[n] = numberCounter.get(n, 0) + 1
        
        threshold = len(nums)//2

        for key, value in numberCounter.items():
            if value > threshold:
                return key
        return -1