class TheSet:
    def __init__(self, capacity):
        self.elements = [None] * capacity
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def get_size(self):
        return self.size

    def contains(self, value):
        for i in range(self.size):
            if self.elements[i] == value:
                return True
        return False

    def add(self, value):
        if not self.contains(value):
            self.elements[self.size] = value
            self.size += 1

    def remove(self, value):
        for i in range(self.size):
            if self.elements[i] == value:
                for j in range(i, self.size - 1):
                    self.elements[j] = self.elements[j + 1]
                self.size -= 1
                return