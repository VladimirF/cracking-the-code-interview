import unittest


class MyQueue:
    def __init__(self):
        self.stack = []
        self.buffer_stack = []

    def enqueue(self, val):
        """
        time complexity O(n)
        size complexity O(n)
        """
        for _ in range(len(self.stack)):
            self.buffer_stack.append(self.stack.pop())

        self.buffer_stack.append(val)
        for _ in range(len(self.buffer_stack)):
            self.stack.append(self.buffer_stack.pop())

    def dequeue(self):
        """
        time complexity O(1)
        size complexity O(1)
        """
        return self.stack.pop()


class Test(unittest.TestCase):
    def test_func(self):
        ss = MyQueue()
        for i in range(1, 11):
            ss.enqueue(i)

        assert ss.stack == [_ for _ in reversed(range(1, 11))]

        values = []
        for _ in range(10):
            values.append(ss.dequeue())
        assert values == [_ for _ in range(1, 11)]


if __name__ == "__main__":
    unittest.main()
