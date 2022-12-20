import unittest

from common.LinkedList import LinkedListNode, LinkedList


def remove_dups(ll: LinkedList) -> LinkedList:
    """
    time complexity: O(n)
    size complexity: O(n)
    """
    seen = set()
    runner = ll.head
    previous = None
    while runner:
        if runner.val not in seen:
            seen.add(runner.val)
            previous = runner
        else:
            previous.next = runner.next
        runner = runner.next
    ll.tail = previous
    return ll


class Test(unittest.TestCase):
    test_cases = (
        (LinkedList(['v', 'o', 'v', 'a']), LinkedList(['v', 'o', 'a'])),
        (LinkedList([1, 1, 1]), LinkedList([1])),
        (LinkedList([1, 2, 3, 3]), LinkedList([1, 2, 3])),
        (LinkedList([1, 1, 1, 2, 2, 3, 3]), LinkedList([1, 2, 3])),
        (LinkedList([]), LinkedList([]))
    )
    testable_functions = [remove_dups]

    def test_string_rotation(self):
        for [ll, expected] in self.test_cases:
            for test_func in self.testable_functions:
                result = test_func(ll)
                assert str(result) == str(expected),\
                    f"failed for value: [{ll}], result is [{result}] expected is [{expected}]"


if __name__ == "__main__":
    unittest.main()

