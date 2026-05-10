class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class TheLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def is_empty(self):
        return self.head is None

    def get_size(self):
        return self.size

    def add(self, value):
        new_node = Node(value)

        if self.is_empty():
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self.size += 1

    def add_first(self, value):
        new_node = Node(value)

        if self.is_empty():
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

        self.size += 1

    def get_first(self):
        return self.head.data

    def get_last(self):
        return self.tail.data

    def remove_first(self):
        if self.is_empty():
            return

        self.head = self.head.next
        if self.head is None:
            self.tail = None

        self.size -= 1

    def remove_last(self):
        if self.is_empty():
            return

        if self.head == self.tail:
            self.head = self.tail = None
        else:
            current = self.head
            while current.next != self.tail:
                current = current.next
            current.next = None
            self.tail = current

        self.size -= 1