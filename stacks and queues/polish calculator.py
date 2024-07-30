
class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, item):
        self.stack.append(item)
    
    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from an empty stack")
        return self.stack.pop()
    
    def is_empty(self):
        return len(self.stack) == 0

def calc(expression):
    stack = Stack()
    tokens = expression.split()
    
    for token in reversed(tokens):
        if token in '+-*/':
            op1 = stack.pop()
            op2 = stack.pop()
            if token == '+':
                stack.push(op1 + op2)
            elif token == '-':
                stack.push(op1 - op2)
            elif token == '*':
                stack.push(op1 * op2)
            elif token == '/':
                stack.push(op1 / op2)
        else:
            stack.push(int(token))
    
    return stack.pop()
