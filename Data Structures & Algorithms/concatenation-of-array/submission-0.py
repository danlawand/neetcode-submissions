class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [-1]*(2*n)
        for i, number in enumerate(nums):
            ans[i] = number
            ans[i+n] = number
        return ans