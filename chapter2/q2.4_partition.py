import unittest

from common.LinkedList import *


def partition(ll: LinkedList, partition_val: int) -> LinkedList:
    """
    time complexity: O(n)
    size complexity: O(n)
    """
    left_ll = LinkedList()
    right_ll = LinkedList()
    for val in ll:
        if val.val < partition_val:
            left_ll.add(val)
        else:
            right_ll.add(val)
    left_ll.tail.next = right_ll.head
    return left_ll


class Test(unittest.TestCase):
    test_cases = (
        (LinkedList([3, 5, 8, 5, 10, 2, 1]), 5, LinkedList([3, 2, 1, 5, 8, 5, 10])),
        (LinkedList([3, 5, 8, 5, 10, 2, 1]), 10, LinkedList([3, 5, 8, 5, 2, 1, 10])),
    )
    testable_functions = [partition]

    def test_partition(self):
        for [ll, par, expected] in self.test_cases:
            for test_func in self.testable_functions:
                result = test_func(ll, par)
                assert str(result) == str(expected), \
                    f"failed for value: [{ll}], result is [{result}] expected is [{expected}]"


if __name__ == "__main__":
    unittest.main()
