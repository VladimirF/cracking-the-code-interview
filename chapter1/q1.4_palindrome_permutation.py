import unittest
from collections import Counter
import string


def clean_phrase(phrase):
    return [c for c in phrase.lower() if c in string.ascii_lowercase]


def palindrome_permutation(phrase: str) -> bool:
    """
    EXAMPLE:
        input: Tact Coa
        output: True (palindrome permutations: "taco cat", "atco cta")
    time complexity: O(n): iterating over phrase several times
    size complexity: O(n): counter and string creation
    """
    phrase = ''.join([i for i in phrase if i.isalpha()])
    counter = Counter(phrase.lower())
    odd_counter = 0
    for val in counter:
        if counter[val] % 2 == 1:
            odd_counter += 1
    return odd_counter <= 1


class Test(unittest.TestCase):
    test_cases = [
        ("Tact Coa", True),
        ("Tact CoaC", False),
        ("vovaa", True),
        ("Vladimir", False),
        ("Tact111 Coa2 2 2  !", True),
        ("aabbccfff", True),
    ]
    testable_functions = [palindrome_permutation]

    def test(self):
        for test_func in self.testable_functions:
            for [test_string, expected] in self.test_cases:
                assert test_func(test_string) == expected, f"{test_func.__name__} failed for value: {test_string}"

if __name__ == "__main__":
    unittest.main()
