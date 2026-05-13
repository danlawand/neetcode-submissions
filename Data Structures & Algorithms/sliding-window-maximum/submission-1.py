class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        ans = []
        q = deque()
        l = r = 0
        while r < n:
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            if l > q[0]:
                q.popleft()
            if r+1 >= k:
                ans.append(nums[q[0]])
                l += 1
            r += 1
        
        return ans


    def _maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # iterate through each substring and finding the maximum in it
        n = len(nums)
        ans = []
        # O(n*k)
        # T(n-k)
        for i in range(n-k+1):
            # T(k)
            ans.append(max(nums[i:i+k]))
        return ans
