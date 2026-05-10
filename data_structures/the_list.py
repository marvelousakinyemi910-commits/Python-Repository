class TheList:
    def __init__(self, capacity):
        self.elements = [None] * capacity
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def get_size(self):
        return self.size

    def add(self, value):
        self.elements[self.size] = value
        self.size += 1

    def get(self, index):
        return self.elements[index]

    def set(self, index, value):
        self.elements[index] = value

    def remove(self, value):
        for i in range(self.size):
            if self.elements[i] == value:
                for j in range(i, self.size - 1):
                    self.elements[j] = self.elements[j + 1]
                self.size -= 1
                return