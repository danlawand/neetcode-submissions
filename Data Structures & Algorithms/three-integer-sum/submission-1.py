class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        hashMap = {}
        for num in nums:    
            hashMap[num] = hashMap.get(num, 0) + 1
        
        n = len(nums)
        unique = set()
        for i in range(n):
            for j in range(i+1, n):
                needed = 0 - nums[i]-nums[j]
                if needed in hashMap:
                    # i == j == needed?
                    # i == needed or j == needed
                    # i != j and needed != j and  needed != i
                    if nums[i] == nums[j] and nums[i] == needed:
                        # 0 0 0
                        if hashMap[0] >= 3:
                            unique.add((0,0,0))
                    elif needed == nums[i] or needed == nums[j]:
                        if hashMap[needed] >= 2:
                            triplets = [nums[i], nums[j], needed]
                            triplets.sort()
                            unique.add(tuple(triplets))
                    else:
                        triplets = [nums[i], nums[j], needed]
                        triplets.sort()
                        unique.add(tuple(triplets))
        result = [list(x) for x in unique]
        return result

    def _threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        unique = set()
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    if nums[i] + nums[j] + nums[k] == 0:
                        triple = (nums[i], nums[j], nums[k])
                        triple.sort()
                        unique.add(triple)
        
        result = [list(x) for x in unique] 
        return result