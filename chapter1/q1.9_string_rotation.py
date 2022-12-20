import unittest


def string_rotation(s1: str, s2: str) -> bool:
    """
    time complexity: O(n)
    size complexity: O(n)
    """
    if len(s1) != len(s2):
        return False

    if s1 in s2 + s2:
        return True

    return False


class Test(unittest.TestCase):

    test_cases = [
        ("waterbottle", "erbottlewat", True),
        ("vova", "avov", True),
        ("nope", "nopenope", False),
    ]
    testable_functions = [string_rotation]

    def test_string_rotation(self):
        for [s1, s2, expected] in self.test_cases:
            for test_func in self.testable_functions:
                result = test_func(s1, s2)
                assert result == expected


if __name__ == "__main__":
    unittest.main()
