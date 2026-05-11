class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        m = len(s2)
        if n > m:
            return False
        
        countS1 = [0]*256
        countS2 = [0]*256
        for c in s1:
            countS1[ord(c)] += 1

        windowSize = n
        for i in range(windowSize):
            countS2[ord(s2[i])] += 0
    
        if self.hasTheSameCount(countS1, countS2):
            return True

        left = 0
        right = windowSize-1
        # O(m*256)
        while right <= m-2:
            countS2[ord(s2[left])] -= 1
            left += 1

            right += 1
            countS2[ord(s2[right])] += 1

            if self.hasTheSameCount(countS1, countS2): # O(256)
                return True
        return False

    # O(256) --> O(1)
    def hasTheSameCount(countS1, countS2) -> bool:
        if len(countS1) != len(countS2):
            return False
        for i in range(len(countS1)):
            if countS1[i] != countS2[i]:
                return False
        return True

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
