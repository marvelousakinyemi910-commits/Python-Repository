import unittest
from the_queue import TheQueue

class TestTheQueue(unittest.TestCase):

    def test_enqueue_dequeue(self):
        q = TheQueue(5)
        q.enqueue(10)
        q.enqueue(20)

        self.assertEqual(10, q.dequeue())
        self.assertEqual(20, q.dequeue())

    def test_peek(self):
        q = TheQueue(5)
        q.enqueue(99)

        self.assertEqual(99, q.peek())

    def test_is_empty(self):
        q = TheQueue(5)
        self.assertTrue(q.is_empty())

        q.enqueue(1)
        self.assertFalse(q.is_empty())

    def test_is_full(self):
        q = TheQueue(2)
        q.enqueue(1)
        q.enqueue(2)

        self.assertTrue(q.is_full())

    def test_overflow(self):
        q = TheQueue(1)
        q.enqueue(1)

        with self.assertRaises(Exception):
            q.enqueue(2)

    def test_underflow(self):
        q = TheQueue(1)

        with self.assertRaises(Exception):
            q.dequeue()

if __name__ == "__main__":
    unittest.main()