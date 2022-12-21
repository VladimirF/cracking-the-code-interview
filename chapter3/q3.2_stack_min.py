import unittest


class StackMin:
    def __init__(self):
        self.min_stack = []
        self.stack = []

    class EmptyStackException(Exception):
        def __init__(self):
            super().__init__("Stack is empty")

    def pop(self):
        if not self.stack:
            raise StackMin.EmptyStackException()
        p = self.stack.pop()
        if self.min_stack and self.min_stack[-1] == p:
            self.min_stack.pop()
        return p

    def push(self, val):
        self.stack.append(val)
        if not self.min_stack:
            self.min_stack.append(val)
        elif val < self.min_stack[-1]:
            self.min_stack.append(val)

    def min(self):
        return self.min_stack[-1] if self.min_stack else None

    def __str__(self):
        return f"stack values are {self.stack}, min is {self.min()}"


class Test(unittest.TestCase):
    def test_min_stack(self):
        s = StackMin()
        assert s.min() is None
        s.push(22)  # [22] min: 22
        assert s.min() == 22
        s.push(40)  # [22, 40] min:22
        assert s.min() == 22
        s.push(1)   # [22, 40, 1] min:1
        assert s.min() == 1
        s.pop()     # [22, 40] min:22
        assert s.min() == 22
        s.pop()     # [22] min:22
        assert s.min() == 22
        s.pop()     # [] min: None
        assert s.min() is None
        try:
            s.pop()
        except Exception as e:
            assert isinstance(e, StackMin.EmptyStackException)


if __name__ == "__main__":
    unittest.main()
