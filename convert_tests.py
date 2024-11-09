import convert
import unittest

class TestCases(unittest.TestCase):
    pass

    # Task 1
    def test_str_to_float_1(self):
        input_string = "21.5"
        expected = 21.5
        actual = convert.str_to_float(input_string)
        self.assertEqual(expected, actual)

    def test_str_to_float_2(self):
        input_string = "Hello"
        expected = None
        actual = convert.str_to_float(input_string)
        self.assertEqual(expected, actual)
