import sys
sys.path.insert(0, '..\src')

import unittest
from pair_people import *

class TestPairPeople(unittest.TestCase):
    def test_is_odd(self):
        self.assertTrue(is_odd(1))
        self.assertTrue(is_odd(3))
        self.assertFalse(is_odd(0))
        self.assertFalse(is_odd(2))

    # TODO: test that an exception is thrown if the set of people (arg) contains less than 2 people

    # TODO: assert that there is one group of three if there are an odd number of people to pair
