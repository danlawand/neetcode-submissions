class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        m = len(s2)
        if n > m:
            return False
        # O(m*n)
        for i in range(m-n+1):
            if self.isPermutation(s1, s2[i:i+n]):
                return True
        return False
    # O(n)
    def isPermutation(self, s1: str, s2: str) -> bool:
        count = [0]*256
        if len(s1) != len(s2):
            return False
        
        for i in range(len(s1)):
            count[ord(s1[i])] += 1
            count[ord(s2[i])] -= 1

        return max(count) == 0 and min(count) == 0
