import unittest
from the_map import TheMap

class TestTheMap(unittest.TestCase):

    def test_put_and_get(self):
        m = TheMap(5)
        m.put("A", 10)
        m.put("B", 20)

        self.assertEqual(10, m.get("A"))
        self.assertEqual(20, m.get("B"))

    def test_update(self):
        maap = TheMap(5)
        maap.put("A", 10)
        maap.put("A", 50)

        self.assertEqual(50, maap.get("A"))

    def test_remove(self):
        maap = TheMap(5)
        maap.put("A", 10)
        maap.put("B", 20)

        maap.remove("A")

        self.assertEqual(-1, maap.get("A"))
        self.assertEqual(1, maap.get_size())

    def test_contains(self):
        maap = TheMap(5)
        maap.put("X", 100)

        self.assertTrue(maap.contains_key("X"))
        self.assertFalse(maap.contains_key("Y"))

    def test_is_empty(self):
        m = TheMap(5)

        self.assertTrue(m.is_empty())

        m.put("A", 1)
        self.assertFalse(m.is_empty())

if __name__ == "__main__":
    unittest.main()