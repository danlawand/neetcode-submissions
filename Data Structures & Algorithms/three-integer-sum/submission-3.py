class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        hashMap = {}
        for num in nums:
            hashMap[num] = hashMap.get(num, 0) + 1
        nums.sort()

        unique = set()
        n = len(nums)
        for i in range(n):
            hashMap[nums[i]] -= 1
            for j in range(i+1, n):
                hashMap[nums[j]] -= 1
                needed = 0 - nums[i] - nums[j]
                if needed in hashMap and hashMap[needed] >= 1:
                    if needed < nums[j]:
                        unique.add((nums[i], needed, nums[j]))
                    else:
                        unique.add((nums[i], nums[j], needed))
                hashMap[nums[j]] += 1
        result = [list(x) for x in unique]
        return result