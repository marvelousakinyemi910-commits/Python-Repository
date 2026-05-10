import unittest
from the_set import TheSet

class TestTheSet(unittest.TestCase):

    def test_add(self):
        s = TheSet(5)
        s.add(1)
        s.add(2)

        self.assertEqual(2, s.get_size())

    def test_no_duplicates(self):
        s = TheSet(5)
        s.add(1)
        s.add(1)

        self.assertEqual(1, s.get_size())

    def test_contains(self):
        s = TheSet(5)
        s.add(10)

        self.assertTrue(s.contains(10))
        self.assertFalse(s.contains(5))

    def test_remove(self):
        s = TheSet(5)
        s.add(1)
        s.remove(1)

        self.assertFalse(s.contains(1))

    def test_is_empty(self):
        s = TheSet(5)
        self.assertTrue(s.is_empty())

        s.add(1)
        self.assertFalse(s.is_empty())

if __name__ == "__main__":
    unittest.main()