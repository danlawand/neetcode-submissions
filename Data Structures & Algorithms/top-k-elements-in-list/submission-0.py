class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = []
        numberCounter = {}
        for number in nums:
            numberCounter[number] = numberCounter.get(number, 0) + 1
        
        temp = []
        for key, value in numberCounter.items():
            temp.append([key, value])
        
        sortedTemp = sorted(temp, key=lambda x: x[1], reverse=True)
        print(sortedTemp)
        ans = [x[0] for x in sortedTemp]
        return ans[:k]
