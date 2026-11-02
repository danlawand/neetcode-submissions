class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for bracket in s:
            if self.isOpenBracket(bracket):
                stack.append(bracket)
            else:
                if not stack or not self.doBracketsMatch(stack.pop(), bracket):
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
