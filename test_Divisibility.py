# test_Divisibility.py
# Tests Temp Converter functions

import unittest
import Divisibility

class KnownValues(unittest.TestCase):
    
    ################################################
    # test divisibility
    ################################################
    # for exception handling
    def test_divisibility_forZeroDivisionErrorHandling(self):
        # Capture the results of the function
        self.assertEquals('error', Divisibility.divisibility(10,0))
    def test_divisibility_forValueErrorHandling(self):
        self.assertEquals('error', Divisibility.divisibility(10, 'five'))
    # for expected results
    def test_divisibility_forEvenlyDivisible(self):
        result = Divisibility.divisibility(21, 3)
        self.assertEquals('divides evenly', result)
    def test_divisibility_forEvenlyDivisible_10_2(self):
        result = Divisibility.divisibility(10, 2)
        self.assertEquals('divides evenly', result)
    def test_divisibility_forNotEvenlyDivisible(self):
        result = Divisibility.divisibility(5,2)
        self.assertEquals("doesn't divide evenly", result)
    def test_divisibility_forNotEvenlyDivisible_7_2(self):
        result = Divisibility.divisibility(7,2)
        self.assertEquals("doesn't divide evenly", result)

# Run the tests
if __name__ == '__main__':
    unittest.main()
