class Solution:
    # Time Complexity O(nˆ2)
    # Auxiliary Memory Usage O(1)
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
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