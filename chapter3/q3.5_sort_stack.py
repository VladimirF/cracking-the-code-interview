import sys
import unittest

from common.Stack import *


class SortStack:
    def __init__(self):
        self.min_stack = Stack()
        self.buffer_stack = Stack()

    def pop(self):
        """
        time complexity O(1)
        size complexity O(1)
        """
        return self.min_stack.pop()

    def peek(self):
        """
        time complexity O(1)
        size complexity O(1)
        """
        return self.min_stack.peek()

    def push(self, val):
        """
        time complexity O(n)
        size complexity O(n)
        """
        while not self.min_stack.is_empty():
            if val > self.min_stack.peek():
                self.buffer_stack.push(self.min_stack.pop())
            else:
                break

        self.min_stack.push(val)

        while not self.buffer_stack.is_empty():
            self.min_stack.push(self.buffer_stack.pop())

    def is_empty(self):
        """
        time complexity O(1)
        size complexity O(1)
        """
        return self.min_stack.is_empty()

    def __str__(self):
        return str(self.min_stack)


class Test(unittest.TestCase):
    def test_func(self):
        ss = SortStack()
        for i in range(1, 11):
            ss.push(i)
        print("ss.min_stack", ss.min_stack)
        print("should be ", [_ for _ in range(10, 0, -1)])

        assert ss.min_stack.stack == [_ for _ in range(10, 0, -1)]

        values = []
        for _ in range(11, 1, -1):
            values.append(ss.pop())
        print("values", values)
        assert values == [_ for _ in range(1, 11)]


if __name__ == "__main__":
    unittest.main()
