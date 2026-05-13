class Solution:
    # 
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # iterate through each substring and finding the maximum in it
        n = len(nums)
        ans = []
        # O(n*k)
        # T(n-k)
        for i in range(n-k+1):
            # T(k)
            ans.append(max(nums[i:i+k]))
        return ans
