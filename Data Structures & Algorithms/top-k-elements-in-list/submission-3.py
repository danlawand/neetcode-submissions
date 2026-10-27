class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numCounterMap = {}
        for num in nums:
            numCounterMap[num] = numCounterMap.get(num, 0) + 1
        
        numCounterList = []
        for key, value in numCounterMap.items():
            numCounterList.append([value, key])
        
        numCounterList.sort(reverse=True)
        output = []
        for idx, pair in enumerate(numCounterList):
            if idx == k:
                break
            output.append(pair[1])
        return output