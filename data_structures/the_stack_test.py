import unittest
from the_stack import TheStack

class TestTheStack(unittest.TestCase):

    def test_push_and_pop(self):
        s = TheStack(5)
        s.push(10)
        s.push(20)

        self.assertEqual(20, s.pop())
        self.assertEqual(10, s.pop())

    def test_peek(self):
        s = TheStack(5)
        s.push(100)

        self.assertEqual(100, s.peek())

    def test_is_empty(self):
        s = TheStack(5)
        self.assertTrue(s.is_empty())

        s.push(1)
        self.assertFalse(s.is_empty())

    def test_is_full(self):
        s = TheStack(2)
        s.push(1)
        s.push(2)

        self.assertTrue(s.is_full())

    def test_overflow(self):
        s = TheStack(1)
        s.push(1)

        with self.assertRaises(Exception):
            s.push(2)

    def test_underflow(self):
        s = TheStack(1)

        with self.assertRaises(Exception):
            s.pop()

if __name__ == "__main__":
    unittest.main()