class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        n = len(s)
        m = len(t)
        if n != m:
            return False

        numCounter = {}
        for i in range(n):
            numCounter[s[i]] = numCounter.get(s[i], 0) + 1
            numCounter[t[i]] = numCounter.get(t[i], 0) - 1
        
        for _, value in numCounter.items():
            if value != 0:
                return False
        return True
 