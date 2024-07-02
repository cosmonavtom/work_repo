class Node:

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node


class Queue:

    def __init__(self, max_queue_size=5, head=None, tail=None):
        '''Инитим "голову", "хвост", а так же максимальный размер очереди'''
        self.head = head
        self.tail = tail
        self.max_queue_size = max_queue_size

    def len_queue(self):
        '''Возвращает длину очереди'''
        count = 0
        current_node = self.head
        while current_node:
            count += 1
            current_node = current_node.next_node
        return count

    def enqueue(self, data):
        '''Добавляем Ноду в очередь. Если очередь пуста, то Нода
        становится первым элементом(ну и последним, естественно)
        Если максимальная длина очереди достигнута - ничего не делаем'''
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            if self.isFull():
                return None
            self.tail.next_node = new_node
        self.tail = new_node

    def dequeue(self):
        '''Удаляем Ноду из очереди, т.е. "голову". Головой становится
        следующая за ней Нода. Если очередь пуста, ничего не делаем'''
        if self.head is None:
            return None
        self.head = self.head.next_node

    def show(self):
        '''Выводим значение всех элементов очереди через пробел'''
        current_node = self.head
        while current_node:
            print(current_node.data, end=' ')
            current_node = current_node.next_node

    def isEmpty(self):
        '''Если очередь пуста возвращает True, иначе False'''
        if self.len_queue() == 0:
            return True
        return False

    def isFull(self):
        '''Если лимит очереди достигнут возвращает True, иначе False'''
        if self.len_queue() == self.max_queue_size:
            return True
        return False


my_queue = Queue()
choice = None
while choice != 0:
    print('\nВыберите метод для работы с очередью!')
    choice = int(input('1-добавить, 2-удалить, 3-показать, 0-выход: '))
    if choice == 1:
        if my_queue.isFull():
            print('Очередь переполнена. Нельзя добавить')
        else:
            new_data = input('Введите новый элемент для добавления: ')
            my_queue.enqueue(new_data)
            print(f'Элемент {new_data} добавлен в конец очереди')
    if choice == 2:
        if my_queue.isEmpty():
            print('Очередь пуста. Нечего удалять')
        else:
            my_queue.dequeue()
            print('Первый элемент очереди удалён')
    if choice == 3:
        if my_queue.isEmpty():
            print('Очередь пуста. Нечего показывать')
        else:
            my_queue.show()
            print()

