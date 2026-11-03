class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        left = 0
        right = 0
        n = len(s)
        longest = 0
        while right < n:
            if s[right] in charSet:
                longest = max(longest, right-left)
                while s[right] in charSet:
                    charSet.remove(s[left])
                    left += 1
            charSet.add(s[right])
            right += 1
        longest = max(longest, right-left)
        return longest
