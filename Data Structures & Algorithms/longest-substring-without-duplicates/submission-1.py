class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashMap = {}
        left = 0
        right = 0
        n = len(s)
        longest = 0
        count = 0
        while right < n:
            if s[right] in hashMap:
                longest = max(longest, count)
                lastIdx = hashMap[s[right]]
                while left <= lastIdx:
                    hashMap.pop(s[left])
                    left += 1
                    count -= 1
            hashMap[s[right]] = right
            count += 1
            right += 1
        longest = max(longest, count)
        return longest
                



    def _lengthOfLongestSubstring(self, s: str) -> int:
        result = 0
        n = len(s)
        for i in range(n):
            unique = set()
            count = 0
            for j in range(i, n):
                if s[j] not in unique:
                    unique.add(s[j])
                    count += 1
                else:
                    break
            result = max(result, count)
        return result


