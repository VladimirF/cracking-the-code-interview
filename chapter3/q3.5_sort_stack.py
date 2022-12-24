import sys
import unittest

from common.Stack import Stack


class SortStack(Stack):
    def __init__(self):
        super().__init__()
        self.buffer_stack = Stack()

    def push(self, val):
        """
        time complexity O(n)
        size complexity O(n)
        """
        while not super().is_empty():
            if val > super().peek():
                self.buffer_stack.push(super().pop())
            else:
                break

        super().push(val)

        while not self.buffer_stack.is_empty():
            super().push(self.buffer_stack.pop())


class Test(unittest.TestCase):
    def test_func(self):
        ss = SortStack()
        for i in range(1, 11):
            ss.push(i)
            assert ss.peek() == 1

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
