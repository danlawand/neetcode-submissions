class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Amortized time O(1)
        numCounterMap = {}
        for num in nums:
            numCounterMap[num] = numCounterMap.get(num, 0) + 1
        
        # O(log n)
        maxHeap = []
        heapq.heapify(maxHeap)
        for key, value in numCounterMap.items():
            heapq.heappush(maxHeap, [-value, key])
        
        # O(log n)
        output = []
        for _ in range(k):
            pair = heapq.heappop(maxHeap)
            output.append(pair[1])
        return output
        