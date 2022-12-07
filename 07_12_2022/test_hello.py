# test runner - script used for writing test case
# test suite - class used for test cases
# test case - class method which the actual test
# unittest - module for writing unit test
# test suite (or) class used for writing cases should take unittest.TestCase as base class
# test cases name should begin with test

import unittest
from hello import is_prime

class MyTestCase(unittest.TestCase):
    def test_prime(self):
        self.assertTrue(is_prime(19))

    def test_non_prime(self):
        self.assertFalse(is_prime(21))
    
if __name__ == '__main__':
    unittest.main() # executes all test cases