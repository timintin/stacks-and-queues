
class Queue:
    def __init__(self):
        self.queue = []
    
    def enqueue(self, item):
        self.queue.append(item)
    
    def dequeue(self):
        if self.is_empty():
            raise IndexError("Dequeue from an empty queue")
        return self.queue.pop(0)
    
    def is_empty(self):
        return len(self.queue) == 0
    
    def size(self):
        return len(self.queue)

def find_survivor(n, k):
    queue = Queue()
    for i in range(1, n + 1):
        queue.enqueue(i)
    
    while queue.size() > 1:
        for _ in range(k - 1):
            queue.enqueue(queue.dequeue())
        queue.dequeue()
    
    return queue.dequeue()
