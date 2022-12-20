import unittest

from common.LinkedList import *


def return_kth_to_last(ll: LinkedList, k: int):
    """
    time complexity: O(n)
    size complexity: O(1)
    """
    fast = slow = ll.head
    while k:
        fast = fast.next
        k -= 1
    while fast:
        fast = fast.next
        slow = slow.next

    return slow.val


class Test(unittest.TestCase):
    test_cases = (
        (LinkedList([1, 2, 3]), 1, 3),
        (LinkedList([1, 2, 3]), 2, 2),
        (LinkedList([1, 2, 3]), 3, 1)
    )
    testable_functions = [return_kth_to_last]

    def test_return_kth_to_last(self):
        for [ll, k, expected] in self.test_cases:
            for test_func in self.testable_functions:
                result = test_func(ll, k)
                assert str(result) == str(expected), \
                    f"failed for value: [{ll}], result is [{result}] expected is [{expected}]"


if __name__ == "__main__":
    unittest.main()
