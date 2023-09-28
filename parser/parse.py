class Parser:
    def __init__(self):
        self.operatorDict = {
            "+":1,
            "-":1,
            "*":2,
            "/":2,
            "**":3
        }

    def forwardparseExpresion(self, expresion):
        operatorStack = Stack()
        outexp = ""

        for character in expresion:
            if character in self.operatorDict:
                outexp += self.pushop(operatorStack, character)
            elif character == "(":
                operatorStack.push(character)
            elif character == ")":
                while(operatorStack.peek()!="("):
                    outexp += operatorStack.pop()
                operatorStack.pop()
            else:
                outexp += character

        while(not operatorStack.isEmpty()):
            outexp += operatorStack.pop()
        return outexp

    def parseExpresion(self, expresion, input_ = "infix", output = "postfix"):
        if input_ == "infix" and output == "postfix":
            return self.forwardparseExpresion(expresion)
        elif input_ == "infix" and output == "prefix":
            return self.forwardparseExpresion(self.reverseexp(expresion))[::-1]

    def reverseexp(self, expresion):
        if not expresion:
            return ""
        if expresion[-1] == "(":
            return ")" + self.reverseexp(expresion[:-1])
        if expresion[-1] == ")":
            return "(" + self.reverseexp(expresion[:-1])
        return expresion[-1] +self.reverseexp(expresion[:-1])

    def pushop(self, stack: Stack, operator):
        if stack.len == 0:
            stack.push(operator)
            return ""
        elif stack.peek() == "(":
            stack.push(operator)
            return ""
        elif self.operatorDict[operator] > self.operatorDict[stack.peek()]:
            stack.push(operator)
            return ""
        else:
            return stack.pop()+self.pushop(stack, operator) 


