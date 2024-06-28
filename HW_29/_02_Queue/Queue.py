class Node:
    '''Создаём класс Нода позволяющий создавать ноды(узлы)'''

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node


class Queue:
    '''Инитим необходимые для очереди "Хвост"(последний элемент) и "Голову"(первый)'''

    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    def enqueue(self, data):
        '''Используя Ноду, добавляем элемент в конец очереди. Если очередь пуста назначаем элемент и
            хвостом и головой, т.к. он один'''
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            self.tail.next_node = new_node
        self.tail = new_node

    def dequeue(self):
        '''Удаляем первый элемент(голову) из очереди и возвращаем его. Если очередь пуста, ничего не делаем'''
        if self.head is None:
            return None
        else:
            dequeue_item = self.head
            self.head = self.head.next_node
        return dequeue_item.data


# my_queue = Queue()
# my_queue.enqueue(1)
# my_queue.enqueue('second')
# my_queue.enqueue('3')
# print(my_queue.dequeue())
# print(my_queue.dequeue())
# print(my_queue.dequeue())
