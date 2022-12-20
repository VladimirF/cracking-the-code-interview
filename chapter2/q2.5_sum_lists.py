import unittest

from common.LinkedList import *


def partition(ll1: LinkedList, ll2: LinkedList) -> LinkedList:
    """
    time complexity: O(n)
    size complexity: O(n)
    """
    n1, n2 = ll1.head, ll2.head
    res = LinkedList()
    carry = 0
    while n1 or n2:
        to_add = 0
        current_sum = carry
        if n1:
            current_sum += n1.val
            n1 = n1.next
        if n2:
            current_sum += n2.val
            n2 = n2.next

        if current_sum <= 9:
            carry = 0
            to_add = current_sum
        else:
            to_add = current_sum % 10
            carry = 1

        res.add(to_add)

    if carry:
        res.add(carry)

    return res


class Test(unittest.TestCase):
    test_cases = (
        (LinkedList([7, 1, 6]), LinkedList([5, 9, 2]), LinkedList([2, 1, 9])),
        (LinkedList([3, 2, 1]), LinkedList([3, 2, 1]), LinkedList([6, 4, 2])),
        (LinkedList([9, 9]), LinkedList([9, 9]), LinkedList([8, 9, 1])),
        (LinkedList([1]), LinkedList([3, 2, 1]), LinkedList([4, 2, 1])),
        (LinkedList([]), LinkedList([]), LinkedList([])),
    )
    testable_functions = [partition]

    def test_partition(self):
        for [ll1, ll2, expected] in self.test_cases:
            for test_func in self.testable_functions:
                result = test_func(ll1, ll2)
                assert str(result) == str(expected), \
                    f"failed for value: [{ll1}], [{ll2}], result is [{result}] expected is [{expected}]"


if __name__ == "__main__":
    unittest.main()
