import unittest

from common.LinkedList import *


def palindrome(ll: LinkedList) -> bool:
    stack = []
    for node in ll:
        stack.append(node.val)

    for node in ll:
        if stack.pop() != node.val:
            return False

    return True


class Test(unittest.TestCase):
    test_cases = (
        (LinkedList([7, 1, 6]), False),
        (LinkedList(['a', 'a', 'x', 'x', 'a', 'a']), True),
        (LinkedList([9, 9]), True),
        (LinkedList([1]), True),
        (LinkedList([]), True),
    )
    testable_functions = [palindrome]

    def test_partition(self):
        for [ll1, expected] in self.test_cases:
            for test_func in self.testable_functions:
                result = test_func(ll1)
                assert str(result) == str(expected), \
                    f"failed for value: [{ll1}], result is [{result}] expected is [{expected}]"


if __name__ == "__main__":
    unittest.main()