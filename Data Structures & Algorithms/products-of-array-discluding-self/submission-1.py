class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        prefix = []
        for number in nums:
            prefix.append(product)
            product *= number
        product = 1
        suffix = [-1 for _ in range(len(nums))]
        for i in range(len(nums)-1, -1, -1):
            suffix[i] = product
            product *= nums[i]
        # 1  2 4 6
    #p    1  1 2 8
    #s    48 24 6 1
    #o    48 24 12 8
        output = []
        for i in range(len(nums)):
            output.append(prefix[i]*suffix[i])
        return output


    # negative zero and positive numbers
    # O(n) linear time consumption
    # Linear O(n) auxiliary memory usage
    def _productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        nonZeroProductOfAll = 1
        zeroCounter = 0
        for number in nums:
            if number == 0:
                zeroCounter += 1
                continue
            nonZeroProductOfAll *= number
        
        for number in nums:
            if number != 0:
                if zeroCounter > 0:
                    output.append(0)
                else:
                    output.append(int(nonZeroProductOfAll/number))
            else:
                if zeroCounter > 1:
                    output.append(0) 
                else:
                    output.append(nonZeroProductOfAll)
        return output
