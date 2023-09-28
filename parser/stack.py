class Stack:
    def __init__(self, stack = None):
        self.stack = stack
        if not stack:
            self.stack = []
        self.len = len(self.stack)
    def peek(self):
        if not self.isEmpty():
            return self.stack[-1]
    
    def push(self, value):
        self.stack.append(value)
        self.len+=1
    
    def pop(self):
        if not self.isEmpty():
            self.len-=1
            return self.stack.pop()

    def isEmpty(self):
        return not bool(self.stack)
        
    def __str__(self):
        return str(self.stack)
    
