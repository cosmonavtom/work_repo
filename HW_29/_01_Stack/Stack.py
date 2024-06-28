class Node:
    '''Создаём класс Нода позволяющий создавать ноды(узлы)'''
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node


class Stack:
    '''Создаём класс Stack для хранения информации типа "FI-LO исаользуя ноды"'''
    def __init__(self, stack_size=5, top=None):
        '''Инитим основные параметры класса. Размер стека и верхний элемент'''
        self.stack_size = stack_size
        self.top = top  # через топ обращаемся к атрибутам ноды

    def push(self, data):
        '''Добавляем элемент в стек если стек ещё не переполнен'''
        if self.size_stack() < self.stack_size:
            new_node = Node(data)
            new_node.next_node = self.top  # та вершина которая была
            self.top = new_node  # переназначаем вершину
        else:
            # print("Стэк переполнен")
            return "Стэк переполнен"

    def pop(self):
        '''Удаляем элемент из стэка, проверяя если есть что удалять(стэк не пустой)'''
        if self.top:
            remove_last = self.top
            self.top = self.top.next_node
            return remove_last.data
        else:
            return "Стэк пуст"

    def is_empty(self):
        '''Проверка стека на наличие хотя бы одного элемента. True - стек пустой'''
        if self.top:
            return False
        else:
            return True

    def is_full(self):
        '''Проверка стека на максимальное заполнение. True - стек полный'''
        if self.stack_size == self.size_stack():
            return True
        else:
            return False

    def clear_stack(self):
        '''Удаляем все элементы из стека. Стек становится пустым'''
        while self.top:
            self.pop()

    def get_data(self, index):
        '''Возвращает значение элемента стека по индексу начиная с верхнего(top).
         Если индекс превышает кол-во элементов стека, сообщает об этом'''
        counter = 0
        stack_item = self.top
        while stack_item:
            if counter == index:
                return stack_item.data
            stack_item = stack_item.next_node
            counter += 1
        return f"Out of range"

    def size_stack(self):
        '''Возвращает размер стека(кол-во элементов)'''
        counter = 0
        stack_item = self.top
        while stack_item:
            counter += 1
            stack_item = stack_item.next_node
        return counter

    def counter_int(self):
        '''Возвращает кол-во целых чисел в стеке'''
        counter = 0
        stack_item = self.top
        while stack_item:
            if isinstance(stack_item.data, int):
                counter += 1
            stack_item = stack_item.next_node
        return counter


# stack = Stack()
# stack.push(1)
# stack.push("sta")
# stack.push(2)
# stack.push(2.5)
# stack.push("sta")
# print(stack.counter_int())
# print(stack.stack_size)
# print(stack.get_data(4))