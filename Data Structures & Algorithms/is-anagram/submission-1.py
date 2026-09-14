class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        charCounter = {}

        n = len(s)
        for idx in range(n):
            if s[idx] not in charCounter:
                charCounter[s[idx]] = 0
            charCounter[s[idx]] += 1

            if t[idx] not in charCounter:
                charCounter[t[idx]] = 0
            charCounter[t[idx]] -= 1
        
        for _, frequency in charCounter.items():
            if frequency != 0:
                return False
        
        return True