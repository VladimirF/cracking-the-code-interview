import unittest

from common.Stack import *


class SetOfStacks:
    def __init__(self, max_stack_size=3):
        self.stacks = []
        self.max_stack_size = max_stack_size

    def push(self, val):
        if not self.stacks:
            new_stack = Stack()
            new_stack.push(val)
            self.stacks.append(new_stack)
        else:
            last_stack = self.stacks[-1]
            if len(last_stack) < self.max_stack_size:
                last_stack.push(val)
            else:
                new_stack = Stack()
                new_stack.push(val)
                self.stacks.append(new_stack)

    def pop(self):
        if not self.stacks:
            raise EmptyStackException

        last_stack = self.stacks[-1]
        val = last_stack.pop()
        if len(last_stack) == 0:
            self.stacks.pop(-1)
        return val

    def __str__(self):
        strs = [str(s) for s in self.stacks]
        return " ".join(strs)


class Test(unittest.TestCase):
    def test_min_stack(self):
        ss = SetOfStacks(3)
        for i in range(10):
            ss.push(i)
        assert str(ss) == "[0, 1, 2] [3, 4, 5] [6, 7, 8] [9]"
        values = []
        for _ in range(10):
            values.append(ss.pop())
        assert values == [_ for _ in reversed(range(10))]


if __name__ == "__main__":
    unittest.main()
