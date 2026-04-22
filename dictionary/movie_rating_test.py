import movie_rating
from unittest import TestCase

class MovieRatingTest(TestCase):

    def test_that_movies_dictionary_is_empty_on_creation(self):
        movies = {}
        self.assertEqual(movies, {})

    def test_that_the_length_of_the_dictionary_is_zero_on_creation(self):
        movies = {}
        self.assertEqual(len(movies),0)
    def test_that_a_movie_is_successfully_added(self):
        movies = {}
        actual = movie_rating.add_movie(movies,"Anikulapo")
        self.assertTrue(actual)
    def test_that_the_length_of_dictionary_is_increased_after_adding_a_movie(self):
        movies = {}
        actual = movie_rating.add_movie(movies,"Anikulapo")
        self.assertEqual(len(movies),1)

    def test_that_duplicate_movies_can_not_be_added(self):
        movies = {}
        movie_rating.add_movie(movies,"Anikulapo")
        actual = movie_rating.add_movie(movies,"Anikulapo")
        self.assertFalse(actual)

    def test_that_a_movie_rating_is_successful(self):
        movies = {}
        movie_rating.add_movie(movies,"Anikulapo")
        actual =  movie_rating.rate_movie(movies,"Anikulapo", 5)
        self.assertTrue(actual)

    def test_that_movie_rating_can_not_exceed_5(self):
        movies = {}
        movie_rating.add_movie(movies,"Anikulapo")
        actual =  movie_rating.rate_movie(movies,"Anikulapo", 8)
        self.assertEqual(actual, "rating must be between 1 and 5")

    def test_that_movie_rating_can_not_be_lower_than_1(self):
        movies = {}
        movie_rating.add_movie(movies,"Anikulapo")
        actual =  movie_rating.rate_movie(movies,"Anikulapo", -2)
        self.assertEqual(actual, "rating must be between 1 and 5")
