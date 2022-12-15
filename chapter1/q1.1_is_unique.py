import unittest
from common.common import get_random_string, get_random_unique_string


def is_unique_set(string: str) -> bool:
    """
    time complexity: O(n) len operation is O(n) , each set insert operation is O(1) thus O(n)
    size complexity: O(n)
    """
    return len(set(string)) == len(string)


def is_unique_inplace(string: str) -> bool:
    """
    time complexity: O(n log n): sorting is O(n log n)
    size complexity: O(1): inplace
    """
    string = sorted(string)
    previous_char = None

    for char in string:
        if char == previous_char:
            return False
        previous_char = char

    return True


def is_unique_ascii(string: str) -> bool:
    """
    time complexity: O(n): iterating over string, each array operations O(1)
    size complexity: O(1): fixed size array is constant size C * O(1), in this case C equals to 128
    """
    if len(string) > 128:
        return False

    seen = [False] * 128
    for char in string:
        ascii_val = ord(char)
        if seen[ascii_val]:
            return False
        seen[ascii_val] = True

    return True


class UnitTests(unittest.TestCase):
    is_unique_impl = [is_unique_set, is_unique_inplace, is_unique_ascii]
    test_cases = [
        ("abc1", True),
        ("vova", False),
        ("Vladimir", False),
        ("", True),
        (get_random_unique_string(52), True),
        (get_random_string(55), False),
    ]

    def test_is_unique_test(self):
        for input_string, expected in self.test_cases:
            print("testing ", input_string)
            for is_unique in self.is_unique_impl:
                assert (is_unique(input_string) == expected), f"{is_unique.__name__} failed for value: {input_string}"


if __name__ == '__main__':
    unittest.main()
