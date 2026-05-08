class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        m = len(s2)
        if n > m:
            return False
        s1Count = [0]*26
        s2Count = [0]*26

        for i in range(n):
            s1Count[ord(s1[i])-ord('a')] += 1
            s2Count[ord(s2[i])-ord('a')] += 1
        
        matches = 0
        for i in range(26):
            if s1Count[i] == s2Count[i]:
                matches += 1
        
        l = 0
        for r in range(n, m):
            if matches == 26:
                return True
            
            idx = ord(s2[r])-ord('a')
            s2Count[idx] += 1
            if s1Count[idx] == s2Count[idx]:
                matches += 1
            elif s1Count[idx]+1 == s2Count[idx]:
                matches -= 1
            
            idx = ord(s2[l])-ord('a')
            s2Count[idx] -=1
            if s1Count[idx] == s2Count[idx]:
                matches += 1
            elif s1Count[idx]-1 == s2Count[idx]:
                matches -= 1
            l+=1
        return matches == 26
            




    
    def _checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        m = len(s2)
        # O(m*n)
        for i in range(m):
            if i+n-1 >= m:
                break
            if self.checkPermutation(s2[i:i+n], s1):
                return True
        return False
    # O(n+256)
    def checkPermutation(self, permutation, s1):
        n = len(s1)
        countChar = [0]*256
        for i in range(n):
            countChar[ord(permutation[i])] += 1
            countChar[ord(s1[i])] -= 1
        
        if min(countChar) != 0 or max(countChar) != 0:
            return False
        return True