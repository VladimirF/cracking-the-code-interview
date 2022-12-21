import unittest

from common.LinkedList import *


def intersection(ll1: LinkedList, ll2: LinkedList) -> LinkedListNode:
    """
    time complexity: O(n1 + n2)
    size complexity: O(1)
    """
    if ll1.tail != ll2.tail:
        return None

    len1 = len2 = 0
    for node in ll1:
        len1 += 1
    for node in ll2:
        len2 += 1

    longer, shorter = (ll1.head, ll2.head) if len1 > len2 else (ll2.head, ll1.head)
    skip = abs(len1 - len2)
    while skip:
        longer = longer.next
        skip -= 1
    while longer is not shorter:
        longer = longer.next
        shorter = shorter.next

    return longer


def intersection_hash(ll1: LinkedList, ll2: LinkedList) -> LinkedListNode:
    """
    time complexity: O(n1 + n2)
    size complexity: O(n1)
    """
    seen_nodes = {node for node in ll1}
    for node in ll2:
        if node in seen_nodes:
            return node
    return None


class Test(unittest.TestCase):
    ll1 = LinkedList([1, 2, 3])
    ll2 = LinkedList([11, 22, 33])
    tail = LinkedList(['t', 'a', 'i', 'l'])
    ll1.tail.next = tail.head
    ll1.tail = tail.tail
    ll2.tail.next = tail.head
    ll2.tail = tail.tail
    test_cases = (
        (ll1, ll2, tail.head),
        (LinkedList([7, 1, 6]), LinkedList([7, 1, 6]), None)
    )
    testable_functions = [intersection_hash, intersection]

    def test_partition(self):
        for [ll1, ll2, expected] in self.test_cases:
            for test_func in self.testable_functions:
                result = test_func(ll1, ll2)
                assert str(result) == str(expected), \
                    f"failed for value: [{str(ll1)}], result is [{result}] expected is [{expected}]"


if __name__ == "__main__":
    unittest.main()
