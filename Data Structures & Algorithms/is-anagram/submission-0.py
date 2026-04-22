class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        n = len(s)
        m = len(t)
        if n != m:
            return False

        charCounter = {}
        for i in range(n):
            charCounter[s[i]] = charCounter.get(s[i], 0) + 1
            charCounter[t[i]] = charCounter.get(t[i], 0) - 1
        
        for key, value in charCounter.items():
            if value != 0:
                return False
        return True