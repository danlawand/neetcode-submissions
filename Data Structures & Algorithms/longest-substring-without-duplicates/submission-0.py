class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
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


