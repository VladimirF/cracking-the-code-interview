import unittest

from common.LinkedList import *


def delete_middle_node(node: LinkedListNode):
    """
    time complexity: O(1)
    size complexity: O(1)
    """
    node.val = node.next.val
    node.next = node.next.next


class Test(unittest.TestCase):
    original_ll = LinkedList([1, 2, 3, 4])
    test_cases = (
        (original_ll.head.next.next, LinkedList([1, 2, 4])),
    )
    testable_functions = [delete_middle_node]

    def test_return_kth_to_last(self):
        for [node_to_delete, expected] in self.test_cases:
            for test_func in self.testable_functions:
                test_func(node_to_delete)
                assert str(self.original_ll) == str(expected), \
                    f"failed for value: [{self.original_ll}], result is [{self.original_ll}] expected is [{expected}]"


if __name__ == "__main__":
    unittest.main()


