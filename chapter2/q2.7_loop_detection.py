import unittest

from common.LinkedList import *


def loop_detection(ll: LinkedList) -> LinkedListNode:
    """
    time complexity: O(n)
    size complexity: O(1)
    """
    slow = fast = ll.head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if fast is slow:
            break

    # no loop
    if fast is None or fast.next is None:
        return None

    # find the loop beginning
    slow = ll.head
    while fast is not slow:
        fast = fast.next
        slow = slow.next

    return fast


class Test(unittest.TestCase):
    def test_loop_detection(self):
        ll_with_loop = LinkedList(["A", "B", "C", "D", "E"])
        loop_start_node = ll_with_loop.head.next.next
        ll_with_loop.tail.next = loop_start_node

        tests = [
            (ll_with_loop, loop_start_node),
            ((LinkedList(('V', 'O', 'V', 'A'))), None)
        ]

        for ll, expected in tests:
            result = loop_detection(ll)
            assert result == expected


if __name__ == "__main__":
    unittest.main()
