class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #   -3  2  1  4  1
        #    1 -3 -6 -6 -24
        #    8  4  4   1  1
        #    8 -12 -24 -6 -24


        #   -3  2  0  4  1
        #    1 -3 -3  0  0
        #    0  0  4  1 1
        #    0  0  -12 0 0
        n = len(nums)
        leftProducts = [1 for _ in range(n)]
        rightProducts = [1 for _ in range(n)]

        for idx in range(1, n):
            leftProducts[idx] = leftProducts[idx-1]*nums[idx-1]
        for idx in range(n-2, -1, -1):
            rightProducts[idx] = rightProducts[idx+1]*nums[idx+1]
        
        output = []

        for idx in range(n):
            output.append(rightProducts[idx]*leftProducts[idx])
        
        return output
