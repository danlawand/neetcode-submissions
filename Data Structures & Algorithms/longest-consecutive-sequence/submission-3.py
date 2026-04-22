class Solution:
    #def longestConsecutive(self, nums: List[int]) -> int:

    # Time Compl. O(n^2)
    # Aux Memory Usage O(1)
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 0:
            return 0
        nums.sort()
        longS = 0
        curr = 1
        prev = nums[0]
        # 1 2 3 8 9 10
        # 1 2 3 1 2  3
        for i in range(1, n):
            if nums[i] == prev:
                continue
            if nums[i]-prev == 1:
                curr += 1
            else:
                longS = max(longS, curr)
                curr = 1
            prev = nums[i]
        longS = max(longS, curr)
        return longS