class Solution:
    # Time complexity O(n)
    # Additional Memory O(n) 
    def hasDuplicate(self, nums: List[int]) -> bool:
        numberCounter = set()
        for num in nums:
            # Avg O(1)
            if num in numberCounter:
                return True
            # O(1)
            numberCounter.add(num)
        return False
