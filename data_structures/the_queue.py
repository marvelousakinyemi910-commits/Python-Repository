class TheQueue:
    def __init__(self, capacity):
        self.queue = [None] * capacity
        self.front = 0
        self.rear = -1
        self.size = 0
        self.capacity = capacity

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.capacity

    def enqueue(self, value):
        if self.is_full():
            raise Exception("Queue is full")
        self.rear += 1
        self.queue[self.rear] = value
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        value = self.queue[self.front]

        # shift elements left
        for i in range(self.rear):
            self.queue[i] = self.queue[i + 1]

        self.rear -= 1
        self.size -= 1
        return value

    def peek(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.queue[self.front]