import unittest


def zero_matrix(matrix):
    """
    time complexity: O(n)
    size complexity: O(m+n)
    """
    m = len(matrix)
    n = len(matrix[0])
    rows_to_zero, columns_to_zero = set(), set()
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                rows_to_zero.add(i)
                columns_to_zero.add(j)

    for i in rows_to_zero:
        for runner in range(n):
            matrix[i][runner] = 0

    for j in columns_to_zero:
        for runner in range(m):
            matrix[runner][j] = 0

    return matrix


class Test(unittest.TestCase):
    test_cases = [
        (
            [
                [1, 2, 3, 4, 0],
                [6, 0, 8, 9, 10],
                [11, 12, 13, 14, 15],
                [16, 0, 18, 19, 20],
                [21, 22, 23, 24, 25],
            ],
            [
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [11, 0, 13, 14, 0],
                [0, 0, 0, 0, 0],
                [21, 0, 23, 24, 0],
            ],
        )
    ]
    testable_functions = [zero_matrix]

    def test_zero_matrix(self):
        for test_func in self.testable_functions:
            for [test_matrix, expected] in self.test_cases:
                test_matrix = test_matrix
                assert test_func(test_matrix) == expected


if __name__ == "__main__":
    unittest.main()
