from stack import Stack

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

    def backwardparseExpresion(self, expresion):
        valueStack = Stack()
        outexp = ""

        for character in expresion:
            if character in self.operatorDict:
                b = valueStack.pop()
                a = valueStack.pop()
                valueStack.push("("+a+character+b+")")
            else:
                valueStack.push(character)
        
        return valueStack.pop()

    def parseExpresion(self, expresion, output = "postfix"):
        if (expresion[0] not in self.operatorDict and expresion[-1] not in self.operatorDict):
            if output == "postfix":
                return self.forwardparseExpresion(expresion)
            if output == "prefix":
                return self.forwardparseExpresion(self.reverseExpresion(expresion))[::-1]
        if expresion[-1] in self.operatorDict:
            if output == "infix":
                return self.backwardparseExpresion(expresion)
            if output == "prefix":
                return self.parseExpresion(self.backwardparseExpresion(expresion), output = "prefix")
        if expresion[0] in self.operatorDict:
            if output == "infix":
                return self.reverseExpresion(self.backwardparseExpresion(expresion[::-1]))
            if output == "postfix":
                return self.forwardparseExpresion(self.parseExpresion(expresion, output = "infix"))

    def reverseExpresion(self, expresion):
        if not expresion:
            return ""
        if expresion[-1] == "(":
            return ")" + self.reverseExpresion(expresion[:-1])
        if expresion[-1] == ")":
            return "(" + self.reverseExpresion(expresion[:-1])
        return expresion[-1] +self.reverseExpresion(expresion[:-1])

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
