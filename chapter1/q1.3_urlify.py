import unittest


def urlify(string: str, length: int) -> str:
    """
    time complexity: O(n) iterating once
    size complexity: O(n) list creation from str
    """
    char_list = list(string)
    write_index = len(char_list)

    for i in reversed(range(length)):
        if char_list[i] == " ":
            char_list[write_index - 3: write_index] = "%20"
            write_index -= 3
        else:
            char_list[write_index - 1] = char_list[i]
            write_index -= 1

    return "".join(char_list)


def urlify_pythonic(string: str, length: int) -> str:
    """
    time complexity: O(n) iterating
    size complexity: O(n) string creation
    """
    return string[:length].replace(" ", "%20")


class UnitTests(unittest.TestCase):
    test_functions = [urlify, urlify_pythonic]
    test_cases = [
        ("Mr John Smith    ", 13, "Mr%20John%20Smith"),
        ("vova", 4, "vova"),
        ("", 0, ""),
    ]

    def test_is_unique_test(self):
        for s1, length, expected in self.test_cases:
            for test_func in self.test_functions:
                result = test_func(s1, length)
                assert (result == expected), f"{test_func.__name__} failed for value: [{s1}], result is [{result}]"


if __name__ == '__main__':
    unittest.main()
