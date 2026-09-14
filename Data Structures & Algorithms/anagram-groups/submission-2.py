class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for s in strs:
            anagram = getAnagramPattern(s)
            if anagram not in anagrams:
                anagrams[anagram] = []
            anagrams[anagram].append(s)
        
        response = []
        for anagramPattern, wordsList in anagrams.items():
            response.append(wordsList)
        return response
    

def getAnagramPattern(s: str) -> str:
    return "".join(sorted(s))