class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for bracket in s:
            if isOpenBracket(bracket):
                stack.append(bracket)
            else:
                if not stack or not doBracketsMatch(stack.pop(), bracket):
                    return False
        
        return len(stack) == 0

def isOpenBracket(s: str) -> bool:
    if s == '[' or s == '(' or s == '{':
        return True
    return False

def doBracketsMatch(s, e) -> bool:
    if s == '[' and e == ']':
        return True
    if s == '(' and e == ')':
        return True
    if s == '{' and e == '}':
        return True
    return False