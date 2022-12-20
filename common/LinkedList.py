class LinkedListNode:
    def __init__(self, val, next_node=None):
        self.val = val
        self.next = next_node

    def __str__(self):
        return str(self.val)


class LinkedList:
    def __init__(self, values=None):
        self.head = None
        self.tail = None
        for v in values:
            self.add(v)

    def add(self, value):
        if self.head is None:
            self.tail = self.head = LinkedListNode(value)
        else:
            self.tail.next = LinkedListNode(value)
            self.tail = self.tail.next
        return self.tail

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def __str__(self):
        values = [str(node) for node in self]
        return " -> ".join(values)
