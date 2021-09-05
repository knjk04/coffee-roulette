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


    def test_pair_raises_exception_when_no_people_to_pair(self):
        with self.assertRaises(ValueError):
            pair({})


    def test_pair_raises_exception_when_one_person_to_pair(self):
        with self.assertRaises(ValueError):
            pair({'Arthur'})

    # TODO: assert that there is one group of three if there are an odd number of people to pair
