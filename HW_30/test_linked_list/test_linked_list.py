import unittest

from ..LinkedListClass import Node, LinkedList


class TestNode(unittest.TestCase):

    def test_00_init_node(self):
        test_node = Node('test_data')
        self.assertEqual(test_node.data, 'test_data')
        self.assertEqual(test_node.next_node, None)


class TestLinkedList(unittest.TestCase):

    def test_01_init(self):
        test_ll = LinkedList()
        self.assertEqual(test_ll.head, None)

    def test_02_insert_at_head(self):
        test_ll = LinkedList()
        test_ll.insert_at_head(1)
        self.assertEqual(test_ll.head.data, 1)
        test_ll.insert_at_head(2)
        self.assertEqual(test_ll.head.data, 2)
        self.assertEqual(test_ll.insert_at_head(3), 'Узел с данными 3 добавлен в начало списка')

    def test_03_insert_at_end(self):
        test_ll = LinkedList()
        test_ll.insert_at_end(1)
        self.assertEqual(test_ll.head.data, 1)
        test_ll.insert_at_end(2)
        self.assertEqual(test_ll.head.next_node.data, 2)
        self.assertEqual(test_ll.insert_at_end(3), 'Узел с данными 3 добавлен в конец списка')

    def test_04_remove_node_position(self):
        test_ll = LinkedList()
        for i in range(1, 5):
            test_ll.insert_at_end(i)
        self.assertEqual(test_ll.remove_node_position(1), 'Удален узел с данными 1 позиции 1')
        self.assertEqual(test_ll.remove_node_position(3), 'Удален узел с данными 4 позиции 3')
        self.assertEqual(test_ll.remove_node_position(5), 'Ничего не удалено')

    def test_05_insert_at_position(self):
        test_ll = LinkedList()
        for i in range(1, 5):
            test_ll.insert_at_end(i)
        self.assertEqual(test_ll.insert_at_position('test_data', 1), 'Узел с данными test_data добавлен на позицию 1')
        self.assertEqual(test_ll.head.data, 'test_data')
        self.assertEqual(test_ll.insert_at_position('test_data_2', 8), None)
        self.assertEqual(test_ll.insert_at_position('test_data_3', 5),
                         'Узел с данными test_data_3 добавлен на позицию 5')

    def test_06_print_ll(self):
        test_ll = LinkedList()
        for i in range(1, 3):
            test_ll.insert_at_position(f'{i}-test', i)
        self.assertEqual(test_ll.head.data, '1-test')
        self.assertEqual(test_ll.head.next_node.data, '2-test')
        self.assertEqual(test_ll.print_ll(), 'Данные списка выведены')

    def test_07_get(self):
        test_ll = LinkedList()
        for i in range(1, 3):
            test_ll.insert_at_position(f'{i}-test', i)
        self.assertEqual(test_ll.get('2-test'), (True, test_ll.head.next_node))
        self.assertEqual(test_ll.get('test'), (False, None))

    def test_08_change_data(self):
        test_ll = LinkedList()
        for i in range(1, 3):
            test_ll.insert_at_position(f'{i}-test', i)
        self.assertEqual(test_ll.change_data('2-test', 'new_test'), 'Заменены данные в узле № 2')
        self.assertEqual(test_ll.change_data('2-test', 'new_test'), 'Данные не обнаружены')













