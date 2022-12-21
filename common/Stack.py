class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.is_empty():
            raise EmptyStackException()
        return self.stack.pop()

    def peek(self):
        return self.stack[-1] if self.stack else None

    def is_empty(self):
        return len(self.stack) == 0

    def __len__(self):
        return len(self.stack)

    def __str__(self):
        return str(self.stack)

    def __bool__(self):
        return bool(self.stack)


class EmptyStackException(Exception):
    def __init__(self):
        super().__init__("Stack is empty")