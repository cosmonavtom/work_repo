import unittest
from ..QueueClass import Queue


class TestQueue(unittest.TestCase):

    def test_01_isEmpty(self):
        test_queue = Queue(3)
        self.assertEqual(test_queue.isEmpty(), True)
        test_queue.enqueue('test_data_1')
        self.assertEqual(test_queue.isEmpty(), False)
        test_queue.enqueue('test_data_2')
        self.assertEqual(test_queue.isEmpty(), False)
        test_queue.enqueue('test_data_3')
        self.assertEqual(test_queue.isEmpty(), False)

    def test_02_isFull(self):
        test_queue = Queue(3)
        self.assertEqual(test_queue.isFull(), False)
        test_queue.enqueue('test_data_1')
        self.assertEqual(test_queue.isFull(), False)
        test_queue.enqueue('test_data_2')
        self.assertEqual(test_queue.isFull(), False)
        test_queue.enqueue('test_data_3')
        self.assertEqual(test_queue.isFull(), True)





