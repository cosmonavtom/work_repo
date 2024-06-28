import unittest
from ._01_Stack.Stack import Node, Stack


class TestNode(unittest.TestCase):

    def test_00_init_node(self):
        test_node = Node('test_data')
        self.assertEqual(test_node.data, 'test_data')
        self.assertEqual(test_node.next_node, None)


class TestStack(unittest.TestCase):

    def test_01_init(self):
        test_stack = Stack(3)
        self.assertEqual(test_stack.stack_size, 3)
        self.assertEqual(test_stack.top, None)

    def test_02_push(self):
        test_stack = Stack(2)
        self.assertEqual(test_stack.top, None)
        test_stack.push('test_push')
        self.assertEqual(test_stack.top.data, 'test_push')
        test_stack.push('test_push_2')
        self.assertEqual(test_stack.top.data, 'test_push_2')
        self.assertEqual(test_stack.push('test_push_3'), 'Стэк переполнен')

    def test_03_pop(self):
        test_stack = Stack()
        test_stack.push('for_remove_test')
        test_data = test_stack.pop()
        self.assertEqual(test_stack.top, None)
        self.assertEqual(test_data, 'for_remove_test')
        self.assertEqual(test_stack.pop(), 'Стэк пуст')

    def test_04_is_empty(self):
        test_stack = Stack()
        self.assertEqual(test_stack.is_empty(), True)
        test_stack.push('test_data')
        self.assertEqual(test_stack.is_empty(), False)

    def test_05_is_full(self):
        test_stack = Stack(3)
        self.assertEqual(test_stack.is_full(), False)
        test_stack.push('test_data_1')
        self.assertEqual(test_stack.is_full(), False)
        test_stack.push('test_data_2')
        self.assertEqual(test_stack.is_full(), False)
        test_stack.push('test_data_3')
        self.assertEqual(test_stack.is_full(), True)

    def test_06_clear_stack(self):
        test_stack = Stack()
        test_stack.push('test_data_1')
        test_stack.push('test_data_2')
        test_stack.push('test_data_3')
        self.assertEqual(test_stack.is_empty(), False)
        test_stack.clear_stack()
        self.assertEqual(test_stack.is_empty(), True)

    def test_07_get_data(self):
        test_stack = Stack()
        test_stack.push('test_data_1')
        test_stack.push('test_data_2')
        test_stack.push('test_data_3')
        self.assertEqual(test_stack.get_data(0), 'test_data_3')
        self.assertEqual(test_stack.get_data(1), 'test_data_2')
        self.assertEqual(test_stack.get_data(2), 'test_data_1')
        self.assertEqual(test_stack.get_data(3), 'Out of range')

    def test_08_size_stack(self):
        test_stack = Stack()
        self.assertEqual(test_stack.size_stack(), 0)
        test_stack.push('test_data_1')
        self.assertEqual(test_stack.size_stack(), 1)
        test_stack.push('test_data_2')
        self.assertEqual(test_stack.size_stack(), 2)
        test_stack.push('test_data_3')
        self.assertEqual(test_stack.size_stack(), 3)

    def test_09_counter_int(self):
        test_stack = Stack()
        self.assertEqual(test_stack.counter_int(), 0)
        test_stack.push('test_data_1')
        self.assertEqual(test_stack.counter_int(), 0)
        test_stack.push(1)
        self.assertEqual(test_stack.counter_int(), 1)
        test_stack.push(0)
        self.assertEqual(test_stack.counter_int(), 2)
        test_stack.push(0.5)
        self.assertEqual(test_stack.counter_int(), 2)
        test_stack.push(-15)
        self.assertEqual(test_stack.counter_int(), 3)







