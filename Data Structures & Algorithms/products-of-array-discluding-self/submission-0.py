class Solution:
    # negative zero and positive numbers
    def productExceptSelf(self, nums: List[int]) -> List[int]:
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
