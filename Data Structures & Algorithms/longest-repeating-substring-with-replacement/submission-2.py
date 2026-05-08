class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        left = 0
        right = 0
        count = {}
        res = 0
        maxF = 0
        maxFChar = s[0]
        while right < n:
            count[s[right]] = count.get(s[right], 0) + 1
            if maxF <= count[s[right]]:
                maxF = count[s[right]]
                maxFChar = s[right]
            
            while right - left + 1 - maxF > k:
                count[s[left]] -= 1
                left += 1
            res = max(res, right-left+1)
            right += 1
        return res
                
