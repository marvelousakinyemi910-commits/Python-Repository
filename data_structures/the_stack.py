class TheStack:
    def __init__(self, capacity):
        self.stack = [None] * capacity
        self.top = -1
        self.capacity = capacity

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == self.capacity - 1

    def size(self):
        return self.top + 1

    def push(self, value):
        if self.is_full():
            raise Exception("Stack is full")
        self.top += 1
        self.stack[self.top] = value

    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        value = self.stack[self.top]
        self.top -= 1
        return value

    def peek(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.stack[self.top]