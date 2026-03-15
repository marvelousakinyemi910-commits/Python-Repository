import random_numbers
from unittest import TestCase

class TestRandomNumbers(TestCase):
    def test_list_length1(self):
        fruits = ["pawpaw","mango","banana","apple","orange"]
        self.assertEqual(random_numbers.list_length(fruits),5)

    def test_list_length2(self):
        numbers = [1,2,3,4,5,6]
        self.assertEqual(random_numbers.list_length(numbers),6)

    def test_sum_even_positions(self):
        numbers = [1,2,3,4,5,6]
        self.assertEqual(random_numbers.sum_even_positions(numbers),9)

    def test_sum_odd_positions(self):
        numbers = [1,2,3,4,5,6]
        self.assertEqual(random_numbers.sum_odd_positions(numbers),12)

    def test_multiply_third_position(self):
        numbers = [1,2,3,4,5,6,7]
        self.assertEqual(random_numbers.multiply_third_position(numbers),28)
        
    def test_average(self):
        numbers = [1,2,3,4,5,6,7]
        self.assertEqual(random_numbers.average(numbers),4)

    def test_largest_element(self):
        numbers = [1,2,3,4,5,6,7]
        self.assertEqual(random_numbers.largest_element(numbers),7)

    def test_smallest_element(self):
        numbers = [1,2,3,4,5,6,7]
        self.assertEqual(random_numbers.smallest_element(numbers),1)
    
    def test_add_third_element(self):
         numbers = [1,2,3,4,5,6,7]
         self.assertEqual(random_numbers.add_third_element(numbers),12)
