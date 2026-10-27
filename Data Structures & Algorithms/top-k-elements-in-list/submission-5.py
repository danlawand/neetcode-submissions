class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Amortized time O(n)
        numCounterMap = {}
        for num in nums:
            # Amortized time O(1)
            numCounterMap[num] = numCounterMap.get(num, 0) + 1
        
        # O(n log n)
        minHeap = []
        heapq.heapify(minHeap)
        for key, value in numCounterMap.items():
            # O(log n)
            heapq.heappush(minHeap, [value, key])
            if len(minHeap) > k:
                # O(log n)
                heapq.heappop(minHeap)
        
        # O(log n)
        output = []
        for _ in range(k):
            pair = heapq.heappop(minHeap)
            output.append(pair[1])
        return output
        