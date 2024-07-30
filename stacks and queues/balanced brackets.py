
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

def is_balanced(s):
    stack = Stack()
    matching_bracket = {')': '(', '}': '{', ']': '['}
    
    for char in s:
        if char in '({[':
            stack.push(char)
        elif char in ')}]':
            if stack.is_empty() or stack.pop() != matching_bracket[char]:
                return False
    
    return stack.is_empty()
