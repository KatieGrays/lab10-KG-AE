# https://github.com/KatieGrays/lab10-KG-AE.git
# Katie Gray & Ariella Efraim

import unittest
import calculator


class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calculator.add(1, 2), 3)
        self.assertEqual(calculator.add(-1, -1), -2)
        self.assertEqual(calculator.add(0, 0), 0)

    def test_subtract(self):

        self.assertEqual(calculator.subtract(2, 1), 1)
        self.assertEqual(calculator.subtract(-1, -1), 0)
        self.assertEqual(calculator.subtract(0, 0), 0)


    ######## Partner 1
    def test_multiply(self):
        self.assertEqual(calculator.mul(2, 3), 6)
        self.assertEqual(calculator.mul(-2, 3), -6)
        self.assertEqual(calculator.mul(0, 3), 0)

    def test_divide(self):
        self.assertEqual(calculator.div(3, 2), 1.5)
        self.assertEqual(calculator.div(-3, 2), -1.5)
        self.assertEqual(calculator.div(0, 2), 0)

    ######## Partner 2
    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            calculator.div(5, 0)

    def test_logarithm(self):
        self.assertAlmostEqual(calculator.logarithm(8, 2), 3)
        self.assertAlmostEqual(calculator.logarithm(16, 2), 4)
        self.assertAlmostEqual(calculator.logarithm(25, 5), 2)

    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            calculator.logarithm(-10, -100)

    ######## Partner 1
    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            calculator.logarithm(0, 5)

    def test_hypotenuse(self):
        self.assertAlmostEqual(calculator.hypotenuse(3, 4), 5)
        self.assertAlmostEqual(calculator.hypotenuse(5, 12), 13)
        self.assertAlmostEqual(calculator.hypotenuse(0, 0), 0)

    def test_sqrt(self):
        self.assertAlmostEqual(calculator.square_root(9), 3.0)
        self.assertAlmostEqual(calculator.square_root(16), 4.0)
        self.assertIsNone(calculator.square_root(-4))

    #     # Test basic function
        #     fill in code
        ##########################

        # Do not touch this

    if __name__ == "__main__":
        unittest.main()
