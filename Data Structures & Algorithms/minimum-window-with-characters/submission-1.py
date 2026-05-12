class Solution:
    # O(n*m)
    def minWindow(self, s: str, t: str) -> str:
        n = len(s)
        m = len(t)
        if m > n:
            return ""
        
        minSize = n
        indexes = [-1,-1]
        
        left = 0
        right = 0
        while right < n:
            if self.doesSubstringContainT(s[left:right+1], t):
                if minSize >= (right-left+1):
                    minSize = right-left+1
                    indexes = [left, right]
                if left == right:
                    right += 1
                left += 1
            else:
                right += 1
        print(indexes)
        return s[indexes[0]: indexes[1]+1]
    
    def doesSubstringContainT(self, s: str, t: str) -> bool:
        if len(t) > len(s):
            return False
        
        countT = [0]*256
        for c in t:
            countT[ord(c)] += 1
        
        for c in s:
            if c in t and countT[ord(c)] > 0:
                countT[ord(c)] -= 1
        
        return max(countT) == 0 and min(countT) == 0
