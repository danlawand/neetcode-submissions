class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        outputs = []
        product = 1
        zeros = 0
        for num in nums:
            if num == 0:
                zeros += 1
                continue
            product *= num

        for num in nums:
            if num == 0:
                if zeros > 1:
                    output = 0
                else:
                    output = product
            elif num < 0:
                if zeros >= 1:
                    output = 0
                else:
                    output = int(product/num)
            else:
                if zeros >= 1:
                    output = 0
                else:
                    output = int(product/num)
            outputs.append(output)
        return outputs
