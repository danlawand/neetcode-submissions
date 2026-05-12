class Solution:
    # O(n*m)
    def minWindow(self, s: str, t: str) -> str:
        n = len(s)
        m = len(t)
        if m > n:
            return ""
        countT, window = {}, {}
        for c in t:
            countT[c] = countT.get(c, 0) + 1

        minSize = n
        indexes = [-1,-1]
        have, need = 0, len(countT)
        left = 0
        right = 0
        while right < n:
            c = s[right]
            window[c] = window.get(c, 0) + 1
            if c in countT and window[c] == countT[c]:
                have += 1
            
            while have == need:
                if minSize >= right - left + 1:
                    indexes = [left, right]
                    minSize = right - left + 1
                window[s[left]] -= 1
                if s[left] in countT and window[s[left]] < countT[s[left]]:
                    have -= 1
                left += 1
            right += 1
        
        return s[indexes[0]:indexes[1]+1]



