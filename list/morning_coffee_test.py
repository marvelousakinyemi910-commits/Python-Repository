import morning_coffee

from unittest import TestCase

class MorningCoffeeTest(TestCase):
    def test_that_a_number_is_a_perfect_square(self):
        self.assertTrue(morning_coffee.perfect_square(16))

    def test_that_a_number_is_not_a_perfect_square(self):
        self.assertFalse(morning_coffee.perfect_square(5))

    def test_that_the_list_of_a_sum_of_digits_returns_the_original_number
