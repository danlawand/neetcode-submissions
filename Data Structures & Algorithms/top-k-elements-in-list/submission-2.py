class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numberCounter = {}
        for number in nums:
            numberCounter[number] = numberCounter.get(number, 0) + 1
        
        frequencyList = []
        for number, frequency in numberCounter.items():
            frequencyList.append([frequency, number])
        
        # O(nlogn)
        frequencyList.sort(reverse=True)
        response = []
        for idx in range(k):
            response.append(frequencyList[idx][1])
        return response