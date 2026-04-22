class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        minLength = len(strs[0])
        for s in strs:
            minLength = min(len(s), minLength)
        # O(n*m)
        for i in range(minLength):
            currentChar = strs[0][i]
            for s in strs:
                if currentChar != s[i]:
                    return prefix
            prefix = prefix + currentChar
        return prefix