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


    def test_one_group_of_three_for_3_people(self):
        odd_number_of_people= {'Alice', 'Bob', 'Claire'}
        pairings = pair(odd_number_of_people)
        self.assertEqual(1, len(pairings))


    def test_one_three_for_5_people(self):
        odd_number_of_people= {'Alice', 'Bob', 'Claire', 'Dave', 'Eve'}
        pairings = pair(odd_number_of_people)

        first = pairings[0]
        second = pairings[1]

        self.assertTrue(len(first) == 3 or len(second) == 3)


    def test_no_threes_for_even_number_of_people(self):
        odd_number_of_people= {'Alice', 'Bob', 'Claire', 'Dave'}
        pairings = pair(odd_number_of_people)

        first_pair = pairings[0]
        second_pair = pairings[1]

        self.assertEqual(2, len(first_pair))
        self.assertEqual(2, len(second_pair))
