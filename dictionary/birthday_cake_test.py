import birthday_cake
from unittest import TestCase

class TestBirthdayCake(TestCase):
    def test_the_addition_of_two_dictionaries(self):
        dictionary_one = { 'a': 1, 'b': 2}
        dictionary_two = {'c': 5, 'e': 6}
        result = {'a': 1, 'b': 2, 'c':5, 'e':6}
        self.assertEqual(birthday_cake.add_two_dictionaries(dictionary_one,dictionary_two),result)
    def test_that_duplicate_keys_is_added_as_one(self):
        dictionary_one = { 'a': 1, 'b': 2}
        dictionary_two = {'c': 5, 'e': 6, 'a' : 2}
        result = {'a': 2, 'b': 2, 'c':5, 'e':6}
        self.assertEqual(birthday_cake.add_two_dictionaries(dictionary_one,dictionary_two),result)

    def test_that_list_is_returned_as_dictionary(self):
        words = ["cat", "dog", "elephant"]
        result = {0: "cat", 1: "dog", 2 : "elephant"}
        self.assertEqual(birthday_cake.length_of_list_as_key(words),result)
