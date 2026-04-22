class Solution:
    def isValid(self, s: str) -> bool:
        parStack = []
        for c in s:
            if self.isOpenBracket(c):
                parStack.append(c)
            else:
                if len(parStack) <= 0:
                    return False
                lastBracket = parStack.pop()
                if not self.isOpenBracket(lastBracket) or not self.areTheSameKindBracket(lastBracket, c): # Same kind and also openBracket
                    return False
        if len(parStack) > 0:
            return False
        return True
    
    def isOpenBracket(self, bracket: str) -> bool:
        if bracket == "{" or bracket == "[" or bracket == "(":
            return True
        return False
    
    def areTheSameKindBracket(self, openBracket: str, closeBracket: str) -> bool:
        if openBracket == "{" and closeBracket == "}":
            return True
        if openBracket == "[" and closeBracket == "]":
            return True
        if openBracket == "(" and closeBracket == ")":
            return True
        return False