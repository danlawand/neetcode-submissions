class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [1 for _ in range(n)]
        suffix = [1 for _ in range(n)]

        for idx in range(1, n):
            prefix[idx] = prefix[idx-1]*nums[idx-1]
        
        for idx in range(n-2, -1, -1):
            suffix[idx] = suffix[idx+1]*nums[idx+1]
        
        output = []
        for idx in range(n):
            output.append(prefix[idx]*suffix[idx])
        
        return output
