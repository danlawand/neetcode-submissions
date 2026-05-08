class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        res = 0
        for i in range(n):
            count = {}
            maxF = 0
            for j in range(i,n):
                count[s[j]] = count.get(s[j],0)+1
                maxF = max(maxF, count[s[j]])
                if j-i+1-maxF <= k:
                    res = max(res, j-i+1)
                else:
                    break 
                
        return res 