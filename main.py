import time
import unittest

def sum(arr):
    s = 0
    for i in arr:
        s += i
    return s

class SumFunctionTest(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(sum([]), 0)

    def test_single_element(self):
        self.assertEqual(sum([42]), 42)

    def test_positive_numbers(self):
        self.assertEqual(sum([1, 2, 3, 4, 5]), 15)

    def test_negative_numbers(self):
        self.assertEqual(sum([-1, -2, -3, -4, -5]), -15)

    def test_mixed_numbers(self):
        self.assertEqual(sum([10, -20, 30, -40, 50]), 30)

    def test_large_numbers(self):
        self.assertEqual(sum([10**10, 10**10, -10**10]), 10**10)

    def test_floating_point_numbers(self):
        self.assertAlmostEqual(sum([1.1, 2.2, 3.3]), 6.6, places=1)

    def test_non_numeric_element(self):
        with self.assertRaises(TypeError):
            sum([1, 2, 'a', 4])

    def test_repeated_numbers(self):
        self.assertEqual(sum([2] * 1000), 2000)

    def test_large_range(self):
        self.assertEqual(sum(range(1, 101)), 5050)

    def test_large_execution_time(self):
        start_time = time.time()
        sum([1] * 10 ** 7)
        execution_time = time.time() - start_time
        self.assertTrue(execution_time < 1)