class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numCounterMap = {}
        for num in nums:
            numCounterMap[num] = numCounterMap.get(num, 0) + 1
        
        heap = []
        # O(n log k)
        for key, value in numCounterMap.items(): # T(n)
            # O(log k)
            heapq.heappush(heap, [value, key])
            if len(heap) > k:
                # O(log k)
                heapq.heappop(heap)
        
        output = []
        for _ in range(k):
            pair = heapq.heappop(heap)
            output.append(pair[1])
        return output