class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Internally it is a hash table, which means the avg case is constant time 
        itemsSet = set()
        for number in nums:
            if number in itemsSet:
                return True
            itemsSet.add(number)
        return False