import unittest
from the_linked_list import TheLinkedList

class TestTheLinkedList(unittest.TestCase):

    def test_add(self):
        link = TheLinkedList()
        link.add("A")
        link.add("B")

        self.assertEqual("A", link.get_first())
        self.assertEqual("B", link.get_last())

    def test_add_first(self):
        link = TheLinkedList()
        link.add("B")

        link.add_first("A")

        self.assertEqual("A", link.get_first())

    def test_remove_first(self):
        link = TheLinkedList()
        link.add("A")
        link.add("B")

        link.remove_first()

        self.assertEqual("B", link.get_first())
        self.assertEqual(1, link.get_size())

    def test_remove_last(self):
        link = TheLinkedList()
        link.add("A")
        link.add("B")

        link.remove_last()

        self.assertEqual("A", link.get_last())
        self.assertEqual(1, link.get_size())

    def test_is_empty(self):
        l = TheLinkedList()

        self.assertTrue(l.is_empty())

        l.add("A")
        self.assertFalse(l.is_empty())

if __name__ == "__main__":
    unittest.main()