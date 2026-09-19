class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        product = 1
        for num in nums:
            prefix.append(product)
            product *= num
        product = 1
        suffix = [-1 for _ in range(len(nums))]

        for i in range(len(nums)-1, -1, -1):
            suffix[i] = product
            product *= nums[i]
        
        output = []
        for i in range(len(nums)):
            output.append(prefix[i]*suffix[i])
        return output
