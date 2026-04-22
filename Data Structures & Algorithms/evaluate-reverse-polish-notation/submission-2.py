class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        opStack = []
        numStack = []
        n = len(tokens)
        for token in tokens:
            if self.isNumber(token):
                numStack.append(int(token))
                continue
            
            n2 = numStack.pop()
            n1 = numStack.pop()

            result = self.applyOperation(n1, n2, token)
            print(result)
            numStack.append(result)

        return numStack.pop()
    
    def _evalRPN(self, tokens: List[str]) -> int:
        opStack = []
        numStack = []
        n = len(tokens)
        for i in range(n-1, -1, -1):
            if self.isNumber(tokens[i]):
                numStack.append(int(tokens[i]))
            else:
                opStack.append(tokens[i])
        
        while opStack:
            op = opStack.pop()
            n1 = numStack.pop()
            n2 = numStack.pop()
            # n1 op n2
            result = self.applyOperation(n1, n2, op)
            print(result)
            numStack.append(result)

        return numStack.pop()
    
    def isNumber(self, s: str) -> bool:
        if s == "+" or s == "-" or s == "*" or s == "/":
            return False
        return True
    
    def applyOperation(self, n1, n2, op):
        if op == "+":
            return n1 + n2
        if op == "-":
            return n1 - n2
        if op == "*":
            return int(n1 * n2)
        return int(float(n1)/n2)

'''
tokens = ["1","2","+","3","*","4","-"]
(1 + 2) * 3 - 4

1 2 3 4
+ * -

["4","13","5","/","+"]

4 13 5 /



13/5
13//5


+ /
5 13 4

4 / 13

5 + 4/13


-, * +
4, 3, 2, 1

op.pop()
+
num.pop()
num.pop()

num.append(result)

1 +2 = 3

-, *
4, 3, 3

*
3 * 3

-
4, 9
n1 = nums.pop()
n2 = nums.pop()

n1 op n2

9-4=5
5 append





'''
