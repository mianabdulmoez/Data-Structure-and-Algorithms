# Stack Implementation (LIFO)
class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, item):
        self.stack.append(item)  # Add item to the top
    
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()  # Remove and return the top item
        return "Stack is empty"
    
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]  # Return the top item without removing it
        return "Stack is empty"
    
    def is_empty(self):
        return len(self.stack) == 0

# Example usage of Stack
s = Stack()
s.push(1)
s.push(2)
s.push(3)
print(s.pop())  # Output: 3 (last in, first out)

# Queue Implementation (FIFO)
class Queue:
    def __init__(self):
        self.queue = []
    
    def enqueue(self, item):
        self.queue.append(item)  # Add item to the rear
    
    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)  # Remove and return the front item
        return "Queue is empty"
    
    def peek(self):
        if not self.is_empty():
            return self.queue[0]  # Return the front item without removing it
        return "Queue is empty"
    
    def is_empty(self):
        return len(self.queue) == 0

# Example usage of Queue
q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.dequeue())  # Output: 1 (first in, first out)
