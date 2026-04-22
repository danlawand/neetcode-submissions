class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = [[strs[0]]]
        n = len(strs)
        anagram = False
        for i in range(1, n):
            for anagramList in ans:
                anagram = self.isAnagram(strs[i], anagramList[0])
                if anagram:
                    anagramList.append(strs[i])
                    break
            if not anagram:
                ans.append([strs[i]])
            anagram = False
        return ans
    
    def isAnagram(self, s0, s1) -> bool:
        if len(s0) != len(s1):
            return False
        charCounter = {}

        for i in range(len(s0)):
            charCounter[s0[i]] = charCounter.get(s0[i], 0) + 1
            charCounter[s1[i]] = charCounter.get(s1[i], 0) - 1
        
        for _, value in charCounter.items():
            if value != 0:
                return False
        return True
            
