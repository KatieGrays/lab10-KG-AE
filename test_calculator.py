# https://github.com/KatieGrays/lab10-KG-AE.git
# Katie Gray & Ariella Efraim

import unittest
import calculator


class TestCalculator(unittest.TestCase):
    ######### Partner 2
    # def test_add(self): # 3 assertions
    #     fill in code

    # def test_subtract(self): # 3 assertions
    #     fill in code
    # ##########################
# hi
    ######## Partner 1
    def test_multiply(self):
        self.assertEqual((2, 3), 6)
        self.assertEqual((-2, 3), 0)  # 3 assertions
        self.assertEqual((-2, 0), 0)

    def test_divide(self):  # 3 assertions
        self.assertEqual((2, 3), 2)
        self.assertEqual((-2, 3), 0)
        self.assertEqual((-2, 0), 0)

    # ##########################

    ######## Partner 2
    # def test_divide_by_zero(self): # 1 assertion
    #     # call division function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     div(0, 5)
    #     fill in code

    # def test_logarithm(self): # 3 assertions
    #     fill in code

    # def test_log_invalid_base(self): # 1 assertion
    #     # use same technique from test_divide_by_zero
    #     fill in code
    # ##########################

    ######## Partner 1
    def test_log_invalid_argument(self):  # 1 assertion
        with self.assertRaises(ValueError):
            calculator.logarithm(0, 5)

    #     fill in code

    def test_hypotenuse(self):  # 3 assertions
        self.assertEqual((2, 3), 2)
        self.assertEqual((-2, 3), 0)
        self.assertEqual((-2, 0), 0)

    def test_sqrt(self):  # 3 assertions
        with self.assertRaises(ValueError):
            self.assertAlmostEqual(calculator.square_root(9), 3.0)
            self.assertAlmostEqual(calculator.square_root(5), 2 ** 0.5)
            self.assertIsNone(calculator.square_root(-4))

    #     # Test basic function
    #     fill in code
    ##########################


# Do not touch this
if __name__ == "__main__":
    unittest.main()