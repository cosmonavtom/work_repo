class Node:
    def __init__(self, data, next_node=None, prev_node=None):
        self.data = data
        self.next_node = next_node
        self.prev_node = prev_node


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_head(self, data):
        new_node = Node(data)
        if self.head is None:
            self.tail = new_node
        else:
            new_node.next_node = self.head  # работа с текущей головой
            self.head.prev_node = new_node  # работа с текущей головой
        self.head = new_node
        return f"Теперь в голове узел с данными {self.head.data}"

    def insert_at_tail(self, data):
        new_node = Node(data)
        if self.head is None:
            # return self.insert_at_head(data)
            self.head = new_node
        else:
            self.tail.next_node = new_node
            new_node.prev_node = self.tail
        self.tail = new_node
        return f"Теперь в хвосте узел с данными {self.tail.data}"

    def remove_from_head(self):
        removed_node = self.head
        self.head = self.head.next_node
        self.head.prev_node = None
        return f"Были удалены данные {removed_node.data} из головы списка.\nТеперь голова списка {self.head.data}"

    def remove_from_tail(self):
        removed_node = self.tail
        self.tail = self.tail.prev_node
        self.tail.next_node = None
        return f"Были удалены данные {removed_node.data} из хвоста списка.\nТеперь хвост списка {self.tail.data}"

    def print_ll_from_head(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next_node
        return "Список выведен с начала"


class AdvancedLinkedList(LinkedList):

    def print_ll_from_tail(self):
        '''Распечатка списка с конца'''
        current_node = self.tail
        while current_node:
            print(current_node.data)
            current_node = current_node.prev_node
        return "Список выведен с конца"

    def len_ll(self):
        '''Возвращает длину списка'''
        current_node = self.head
        count = 0
        while current_node:
            current_node = current_node.next_node
            count += 1
        return count

    def insert_at_index(self, index, data):
        '''Вставляет элемент в список по индексу'''
        new_node = Node(data)
        if index > (self.len_ll() - 1):
            self.insert_at_tail(data)
        elif index == 0:
            self.insert_at_head(data)
        else:
            current_index = 0
            current_node = self.head
            while current_index < index:
                current_node = current_node.next_node
                current_index += 1
            current_node.prev_node.next_node = new_node
            new_node.prev_node = current_node.prev_node
            new_node.next_node = current_node
            current_node.prev_node = new_node

    def remove_node_index(self, index):
        '''Удаляет элемент по индексу'''
        if index > (self.len_ll() - 1):
            self.remove_from_tail()
        elif index == 0:
            self.remove_from_head()
        else:
            current_index = 0
            current_node = self.head
            while current_index < index:
                current_node = current_node.next_node
                current_index += 1
            current_node.next_node.prev_node = current_node.prev_node
            current_node.prev_node.next_node = current_node.next_node

    def remove_node_data(self, data):
        '''Удаляет элемент по данным узла'''
        index = 0
        remove_node = self.head
        while index < (self.len_ll()-1):
            if data == remove_node.data:
                break
            index += 1
            remove_node = remove_node.next_node
        if data != remove_node.data:
            return print(f'Элемент "{data}" не найден')
        if index == 0:
            self.remove_from_head()
        elif index == (self.len_ll() - 1):
            self.remove_from_tail()
        else:
            remove_node.next_node.prev_node = remove_node.prev_node
            remove_node.prev_node.next_node = remove_node.next_node

    def contains_from_head(self, data):
        '''Проверка на содержание элемента с головы списка'''
        current_node = self.head
        while current_node:
            if data == current_node.data:
                return True
            current_node = current_node.next_node
        return False

    def contains_from_tail(self, data):
        '''Проверка на содержание элемента с конца списка'''
        current_node = self.tail
        while current_node:
            if data == current_node.data:
                return True
            current_node = current_node.prev_node
        return False

    def contains_from(self, data, side='head'):
        '''Проверка на содержание элемента по выбору пользователя. head/tail'''
        if side == 'head':
            contain = self.contains_from_head(data)
        elif side == 'tail':
            contain = self.contains_from_tail(data)
        else:
            return f'Ошибка параметра, side может быть только "head" или "tail"'
        return contain


