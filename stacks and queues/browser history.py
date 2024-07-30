
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

class BrowserHistory:
    def __init__(self):
        self.back_stack = Stack()
        self.forward_stack = Stack()

    def visit(self, url):
        self.back_stack.push(url)
        self.forward_stack = Stack()  # Clear forward stack

    def back(self):
        if self.back_stack.is_empty():
            raise IndexError("No pages in back history")
        url = self.back_stack.pop()
        self.forward_stack.push(url)
        return url

    def forward(self):
        if self.forward_stack.is_empty():
            raise IndexError("No pages in forward history")
        url = self.forward_stack.pop()
        self.back_stack.push(url)
        return url
