import unittest
from ._02_Queue.Queue import Node, Queue


class TestNode(unittest.TestCase):

    def test_00_init_node(self):
        test_node = Node('test_data')
        self.assertEqual(test_node.data, 'test_data')
        self.assertEqual(test_node.next_node, None)


class TestQueue(unittest.TestCase):

    def test_01_init(self):
        test_queue = Queue()
        self.assertEqual(test_queue.head, None)
        self.assertEqual(test_queue.tail, None)

    def test_02_enqueue(self):
        test_queue = Queue()
        test_queue.enqueue('test_enqueue')
        self.assertEqual(test_queue.head.data, 'test_enqueue')
        self.assertEqual(test_queue.tail.data, 'test_enqueue')
        test_queue.enqueue('test_enqueue_2')
        self.assertEqual(test_queue.head.data, 'test_enqueue')
        self.assertEqual(test_queue.tail.data, 'test_enqueue_2')

    def test_03_dequeue(self):
        test_queue = Queue()
        test_queue.enqueue('test_enqueue_1')
        test_queue.enqueue('test_enqueue_2')
        test_queue.enqueue('test_enqueue_3')
        test_queue.dequeue()
        self.assertEqual(test_queue.head.data, 'test_enqueue_2')
        self.assertEqual(test_queue.tail.data, 'test_enqueue_3')
        test_queue.dequeue()
        self.assertEqual(test_queue.head.data, 'test_enqueue_3')
        self.assertEqual(test_queue.tail.data, 'test_enqueue_3')
        test_queue.dequeue()
        self.assertEqual(test_queue.head, None)
   


