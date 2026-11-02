class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # O(n log n)
        nums.sort()

        count = dict()
        for num in nums:
            count[num] = count.get(num, 0)+1
        
        output = []
        for i in range(len(nums)):
            count[nums[i]] -= 1
            if i and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, len(nums)):
                count[nums[j]] -= 1
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                target = -(nums[i]+nums[j])
                if target in count and count[target] > 0:
                    output.append([nums[i], nums[j], target])
            
            for j in range(i+1,len(nums)):
                count[nums[j]] += 1
        return output
        
             
