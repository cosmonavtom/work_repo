class Node:
    '''Создаём класс Node'''

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node


class LinkedList:
    '''Класс инициализируемый только "головой"(односвязный)'''

    def __init__(self):
        self.head = None

    def insert_at_head(self, data):
        '''Создаём новый узел и вставляем в начало списка. Есть проверка на пустой список.
        Возвращаем сообщение с добавленными данными'''
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next_node = self.head
            self.head = new_node
        return f"Узел с данными {new_node.data} добавлен в начало списка"

    def insert_at_end(self, data):
        '''Вставляем новый узел в конец списка. Есть проверка на пустой список, тогда
        созданный узел становится началом(ну и концом) списка.
        Возвращаем сообщение с добавленными данными'''
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current_node = self.head
        while current_node.next_node:
            current_node = current_node.next_node
        current_node.next_node = new_node
        return f"Узел с данными {new_node.data} добавлен в конец списка"

    def remove_node_position(self, rm_position):
        '''Удаляем узел по его позиции. Счёт начинается от 1, а не от 0. Получаем позицию
        удаляемой ноды. Сразу проверка на то, что это первая позиция и удаляем в таком случае
        "голову". В ином случае мотаем список до необходимой позиции минус 1. Это облегчит
        перепривязку ссылок на ноды дальше. Далее пропускаем "удаляемую" ноду и делаем привязку
        через неё. Возвращаем сообщение с данными удаленной ноды и ее позицией '''
        if rm_position == 1:
            removed_node = self.head
            self.head = self.head.next_node
            return f"Удален узел с данными {removed_node.data} позиции {rm_position}"
        current_node = self.head
        current_node_position = 1
        while current_node is not None and current_node_position < rm_position - 1:
            current_node = current_node.next_node
            current_node_position += 1
        if current_node is None or current_node.next_node is None:
            return "Ничего не удалено"
        removed_node = current_node.next_node
        current_node.next_node = current_node.next_node.next_node  # removed_node.next_node
        return f"Удален узел с данными {removed_node.data} позиции {rm_position}"

    def insert_at_position(self, data, node_position):
        '''Добавляем элемент по номеру позиции(начиная от 1). Сразу проверка на 1ую позицию
        и в это случае используем метод insert_at_head(). Иначе перебираем список до нужной
        нам позиции минус 1. Если номер позиции превышает длину списка возвращаем None, или
        *опционально* добавляем в конец списка. Иначе вставляем ноду, переназначая ссылку у
        предыдущей на новую, а у новой назначая на следующую. Возвращаем сообщение с данными
        новой ноды и её позицией'''
        new_node = Node(data)
        if node_position == 1:
            self.insert_at_head(data)
            # new_node.next_node = self.head
            # self.head = new_node
            return f"Узел с данными {new_node.data} добавлен на позицию {node_position}"
        """Опционально"""
        current_node = self.head
        # if node_position > self.len_ll():
        #     self.insert_at_end(data)
        #     # while current_node.next_node:
        #     #     current_node = current_node.next_node
        #     # current_node.next_node = new_node
        #     return
        current_node_position = 1
        while current_node is not None and current_node_position < node_position - 1:
            current_node = current_node.next_node
            current_node_position += 1
        """Если есть опционально (код выше то следующие 2 строки не нужны)"""
        if current_node is None:
            return None
        new_node.next_node = current_node.next_node
        current_node.next_node = new_node
        return f"Узел с данными {new_node.data} добавлен на позицию {node_position}"

    def print_ll(self):
        '''Проходимся по всему списку с начала и выводим данные элементов. В конце
        возвращаем сообщение - "Данные списка выведены"'''
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next_node
        return "Данные списка выведены"

    def get(self, data):
        '''Проверяем существование данных в списке. Начинаем проверку с голову списка
        и последовательно идём по нему. Если данные найдены, то возвращаем True и ссылку
        на ноду. Если нет, то False и None. Если в списке есть одинаковые данные, то
        находится только их первое вхождение в список'''
        current_node = self.head
        while current_node:
            if current_node.data == data:
                return True, current_node
            current_node = current_node.next_node
        return False, None

    def change_data(self, node_data, change_data):
        '''Принимаем значение которое надо заменить и на которое. Идём по списку и ищем
        необходимые данные. При нахождении меняем их и возвращаем строку с сообщением об
        этом. Если данные не найдены, так же возвращаем сообщение об этом'''
        current_node = self.head
        current_node_position = 1
        while current_node:
            if current_node.data == node_data:
                current_node.data = change_data
                return f"Заменены данные в узле № {current_node_position}"
            current_node = current_node.next_node
            current_node_position += 1
        return "Данные не обнаружены"

    # def change_data(self, node_data, change_data):
    """Это второй способ для примера"""
    #     result, current_node = self.get(node_data)
    #     if result:
    #         current_node.data = change_data
    #         return "Данные изменены!"
    #     return "Данные не обнаружены"
