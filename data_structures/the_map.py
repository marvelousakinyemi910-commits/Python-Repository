class TheMap:
    def __init__(self, capacity):
        self.keys = [None] * capacity
        self.values = [None] * capacity
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def get_size(self):
        return self.size

    def put(self, key, value):
        # update if exists
        for i in range(self.size):
            if self.keys[i] == key:
                self.values[i] = value
                return

        # add new
        self.keys[self.size] = key
        self.values[self.size] = value
        self.size += 1

    def get(self, key):
        for i in range(self.size):
            if self.keys[i] == key:
                return self.values[i]
        return -1

    def remove(self, key):
        for i in range(self.size):
            if self.keys[i] == key:
                for j in range(i, self.size - 1):
                    self.keys[j] = self.keys[j + 1]
                    self.values[j] = self.values[j + 1]
                self.size -= 1
                return

    def contains_key(self, key):
        return self.get(key) != -1