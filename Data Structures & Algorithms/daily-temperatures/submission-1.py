class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0]*len(temperatures)
        tempStack = []
        for i, temp in enumerate(temperatures):
            while tempStack and temp > tempStack[-1][0]:
                topTemp, topIdx = tempStack.pop()
                result[topIdx] = i-topIdx
            tempStack.append((temp, i))
        return result

    # Time Complexity O(nˆ2)
    # Auxiliary Memory Usage O(1)
    def _dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = []
        n = len(temperatures)
        for i in range(n):
            currTemp = temperatures[i]
            warmerTemp = 0
            for j in range(i, n):
                if temperatures[j] > currTemp:
                    warmerTemp = j-i
                    break
            result.append(warmerTemp)
        return result