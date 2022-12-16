import unittest
from collections import Counter


def check_permutation_counter(s1: str, s2: str) -> bool:
    """
    time complexity: O(n) constructing both Counters is 2 * O(n) => O(n)
    size complexity: O(n) Counters size
    """
    if len(s1) != len(s2):
        return False
    return Counter(s1) == Counter(s2)


def check_permutation_sorting(s1: str, s2: str) -> bool:
    """
    time complexity: O(n log n): sorting is O(n log n)
    size complexity: O(1) inplace
    """
    if len(s1) != len(s2):
        return False
    s1, s2 = sorted(s1), sorted(s2)
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            return False
    return True


class UnitTests(unittest.TestCase):
    test_functions = [check_permutation_sorting, check_permutation_counter]
    test_cases = [
        ("abc1", "b1ca", True),
        ("vova", "vovachka", False),
        ("", "", True),
        (" ", "", False),
    ]

    def test_is_unique_test(self):
        for s1, s2, expected in self.test_cases:
            print("testing ", s1, s2)
            for test_func in self.test_functions:
                assert (test_func(s1, s2) == expected), f"{test_func.__name__} failed for value: {s1} {s2}"


if __name__ == '__main__':
    unittest.main()
