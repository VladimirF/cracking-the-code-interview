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

    def __len__(self):
        return len(self.min_stack)


class Test(unittest.TestCase):
    def test_func(self):
        ss = SortStack()
        for i in range(1, 11):
            ss.push(i)

        assert ss.min_stack.stack == [_ for _ in range(10, 0, -1)]

        values = []
        for _ in range(11, 1, -1):
            values.append(ss.pop())

        assert values == [_ for _ in range(1, 11)]

    def test_push_one(self):
        stack = SortStack()
        stack.push(1)
        assert len(stack) == 1

    def test_push_two(self):
        stack = SortStack()
        stack.push(1)
        stack.push(2)
        assert len(stack) == 2

    def test_push_three(self):
        stack = SortStack()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        assert len(stack) == 3

    def test_pop_one(self):
        stack = SortStack()
        stack.push(1)
        assert stack.pop() == 1

    def test_pop_two(self):
        stack = SortStack()
        stack.push(1)
        stack.push(2)
        assert stack.pop() == 1
        assert stack.pop() == 2

    def test_pop_three(self):
        stack = SortStack()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        assert stack.pop() == 1
        assert stack.pop() == 2
        assert stack.pop() == 3

    def test_push_mixed(self):
        stack = SortStack()
        stack.push(3)
        stack.push(2)
        stack.push(1)
        stack.push(4)
        assert stack.pop() == 1
        assert stack.pop() == 2
        assert stack.pop() == 3
        assert stack.pop() == 4


if __name__ == "__main__":
    unittest.main()
