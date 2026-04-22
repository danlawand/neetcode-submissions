class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = []
        numberCounter = {}
        for number in nums:
            numberCounter[number] = numberCounter.get(number, 0) + 1
        
        temp = []
        for key, value in numberCounter.items():
            temp.append([value, key])
        
        temp.sort()

        for i in range(k):
            ans.append(temp.pop()[1])
        return ans
