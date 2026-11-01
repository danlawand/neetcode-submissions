class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numberCounter = dict()
        # O (n)
        for num in nums:
            numberCounter[num] = numberCounter.get(num, 0) + 1
        
        heap = []
        # O(n log k)
        for key, value in numberCounter.items():
            # O(log k)
            heapq.heappush(heap, [value, key])
            if len(heap) > k:
                # O (log k)
                heapq.heappop(heap)
        
        
        output = []
        # O (k)
        for pair in heap:
            output.append(pair[1])
        
        return output