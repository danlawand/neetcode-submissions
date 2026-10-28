class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        leftProducts = [1 for _ in range(n)]
        rightProducts = [1 for _ in range(n)]

        for idx in range(1, n):
            leftProducts[idx] = nums[idx-1]*leftProducts[idx-1]
        
        for idx in range(n-2, -1, -1):
            rightProducts[idx] = nums[idx+1]*rightProducts[idx+1]
        
        output = []
        for idx in range(n):
            output.append(rightProducts[idx]*leftProducts[idx])
        
        return output