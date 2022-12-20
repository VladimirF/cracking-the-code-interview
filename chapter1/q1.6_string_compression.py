import unittest


def string_compression(phrase: str) -> str:
    if len(phrase) <= 2:
        return phrase

    list_of_char_and_count = []
    current_count = 1
    previous_char = None
    for i, char in enumerate(phrase):
        if char == previous_char:
            current_count += 1
        elif previous_char:
            list_of_char_and_count.append(previous_char + str(current_count))
            current_count = 1
        # last char
        previous_char = char

    list_of_char_and_count.append(previous_char + str(current_count))
    res = "".join(list_of_char_and_count)

    return res if len(res) < len(phrase) else phrase


class Test(unittest.TestCase):
    test_cases = [
        ("aaabbbcccdf", "a3b3c3d1f1"),
        ("vova", "vova"),
        ("111122", "1422"),
        ("xyz", "xyz"),
        ("bbbbb", "b5"),
        ("", ""),
    ]
    testable_functions = [
        string_compression,
    ]

    def test_string_compression(self):
        for test_func in self.testable_functions:
            for test_string, expected in self.test_cases:
                res = test_func(test_string)
                assert res == expected, f"{test_func.__name__} failed for value: {test_string}, result: {res}"


if __name__ == "__main__":
    unittest.main()
