import unittest
import calc             # in the same directory

class TestCalc(unittest.TestCase):              # inheriting a lot of testing capabilities from unittest.TestCase

    # def test_add(self):                         # just like any methods in a class, takes self as the 1st argument
    #     result = calc.add(10, 5)
    #     self.assertEqual(result, 15)

    def add_test(self):                         # doesn't runs since all tests should start 'test_' naming convention
        result = calc.add(10, 5)
        self.assertEqual(result, 15)

    def test_add(self):                                 # usually want to test edge cases
        self.assertEqual(calc.add(10, 5), 15)
        self.assertEqual(calc.add(-1, 1), 0)
        self.assertEqual(calc.add(-1, -1), -2)

    def test_subtract(self):
        self.assertEqual(calc.subtract(10, 5), 5)
        self.assertEqual(calc.subtract(-1, 1), -2)
        self.assertEqual(calc.subtract(-1, -1), 0)

    def test_multiply(self):
        self.assertEqual(calc.multiply(10, 5), 50)
        self.assertEqual(calc.multiply(-1, 1), -1)
        self.assertEqual(calc.multiply(-1, -1), 1)

    def test_divide(self):
        self.assertEqual(calc.divide(10, 5), 2)
        self.assertEqual(calc.divide(-1, 1), -1)
        self.assertEqual(calc.divide(-1, -1), 1)
        self.assertEqual(calc.divide(5, 2), 2.5)                # test floor division // regular division

        # self.assertRaises(ValueError, calc.divide, 10, 0)
        with self.assertRaises(ValueError):                     # using context manager looks better
            calc.divide(10, 0)


    # def test_something(self):
    #     self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
""" basically it is just saying that if we run this öodule directly then run the code withind the conditional """

""" BEST PRACTICES:
    - tests should be isolated -- test shouldn't rely on other test or effect other test and should be able to run
                                  any test by itself independent of the other tests
    - we were adding test to an existing code:
    Test Driven Development --> write the test before you write the code
    
    - any testing is better than no testing --> basic assertions is better than not having anything 
    """