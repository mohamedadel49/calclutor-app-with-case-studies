import unittest
from calculator import add, sub, mul, div


class TestCalculatorCaseStudies(unittest.TestCase):
    # Case Study 1: Addition (add)
    def test_add_positive_numbers(self):
        self.assertEqual(add(10, 5), 15)

    def test_add_negative_and_zero(self):
        self.assertEqual(add(-4, 4), 0)
        self.assertEqual(add(-7, 0), -7)

    # Case Study 2: Subtraction (sub)
    def test_sub_positive_result(self):
        self.assertEqual(sub(10, 4), 6)

    def test_sub_negative_result(self):
        self.assertEqual(sub(4, 10), -6)

    # Case Study 3: Multiplication (mul)
    def test_mul_standard(self):
        self.assertEqual(mul(6, 7), 42)

    def test_mul_by_zero_and_negatives(self):
        self.assertEqual(mul(99, 0), 0)
        self.assertEqual(mul(-3, -5), 15)

    # Case Study 4: Division (div)
    def test_div_standard_and_decimal(self):
        self.assertEqual(div(20, 4), 5.0)
        self.assertAlmostEqual(div(5, 2), 2.5)

    def test_div_by_zero_raises_error(self):
        with self.assertRaises(ValueError):
            div(10, 0)


if __name__ == "__main__":
    unittest.main()
