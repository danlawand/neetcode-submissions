class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        n = len(s)
        if n%2 != 0:
            return False

        for bracket in s:
            if self.isOpenBracket(bracket):
                stack.append(bracket)
            else:
                if len(stack) <= 0:
                    return False
                openBracket = stack.pop()
                if not self.doBracketsMatch(openBracket, bracket):
                    return False        
        return len(stack) == 0
    
    def isOpenBracket(self, bracket: str) -> bool:
        openBrackets = ['{', '[', '(']
        return bracket in openBrackets
    
    def doBracketsMatch(self, openBracket: str, closeBracket: str) -> bool:
        if openBracket == '{':
            return closeBracket == '}'
        elif openBracket == '[':
            return closeBracket == ']'
        else:
            return closeBracket == ')'
