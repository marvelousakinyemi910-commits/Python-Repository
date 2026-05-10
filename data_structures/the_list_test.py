import unittest
from the_list import TheList

class TestTheList(unittest.TestCase):

    def test_add_and_get(self):
        lis = TheList(5)
        lis.add("A")
        lis.add("B")

        self.assertEqual("A", lis.get(0))
        self.assertEqual("B", lis.get(1))

    def test_set(self):
        lis = TheList(5)
        lis.add("A")

        lis.set(0, "Z")

        self.assertEqual("Z", lis.get(0))

    def test_remove(self):
        lis = TheList(5)
        lis.add("A")
        lis.add("B")

        lis.remove("A")

        self.assertEqual(1, lis.get_size())
        self.assertEqual("B", lis.get(0))

    def test_size(self):
        lis = TheList(5)

        self.assertEqual(0, lis.get_size())

        lis.add("A")
        self.assertEqual(1, lis.get_size())

    def test_is_empty(self):
        lis = TheList(5)

        self.assertTrue(lis.is_empty())

        lis.add("A")
        self.assertFalse(lis.is_empty())

if __name__ == "__main__":
    unittest.main()