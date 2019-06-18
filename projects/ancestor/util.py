class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        #  Why is using an array inefficient for this queue class?
        #  - B/c deletion = O(n)
        #  Why don't we care?
        #  - B/c we have a small dataset
        #  - Tradeoff: Readability > runtime complexity optimization
        if self.size() > 0:
            return self.queue.pop(0)  
        else:
            return None
    def size(self):
        return len(self.queue)

class Stack():
    #  This is optimal for this Stack class
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)