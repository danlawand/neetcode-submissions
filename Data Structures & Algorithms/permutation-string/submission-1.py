class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        m = len(s2)

        for i in range(m):
            if i+n-1 >= m:
                break
            if self.checkPermutation(s2[i:i+n], s1):
                return True
        return False
    
    def checkPermutation(self, permutation, s1):
        n = len(s1)
        countChar = [0]*256
        for i in range(n):
            countChar[ord(permutation[i])] += 1
            countChar[ord(s1[i])] -= 1
        
        if min(countChar) != 0 or max(countChar) != 0:
            return False
        return True