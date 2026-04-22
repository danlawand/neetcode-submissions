class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) <= 0:
            return "None"
        ans = ""
        for s in strs:
            stringSizeEncoded = self.encodeStringSize(len(s))
            ans = ans + stringSizeEncoded
            for c in s:
                cInt = ord(c)
                if ord(c) == 255:
                    cInt = -1
                ans = ans+ chr(cInt+1)
        return ans

    def decode(self, s: str) -> List[str]:
        if s == "None":
            return []
        ans = []
        index = 0
        while index < len(s):
            stringSizeText = ""
            while s[index] != " ":
                stringSizeText = stringSizeText + s[index]
                index += 1
            index += 1
            stringStart = index
            stringSize = int(stringSizeText)
            temp = ""
            for c in s[stringStart:stringSize+stringStart]:
            # 5 _ h e l l o 5 0 _  w  o  r  l  d
            # 0 1 2 3 4 5 6 7 8 9  10 11
                cInt = ord(c)
                if ord(c) == 0:
                    cInt = 256
                temp = temp+ chr(cInt-1)
                index += 1
            ans.append(temp)
        return ans
    
    def encodeStringSize(self, stringSize: int) -> str:
        # 0
        # 3
        # 37
        # 370
        if stringSize == 0:
            return "0 "
        ans = ""
        while stringSize > 0:
            number = stringSize%10
            ans = f"{number}" + ans
            stringSize = stringSize//10
        ans=ans+" "
        return ans

 