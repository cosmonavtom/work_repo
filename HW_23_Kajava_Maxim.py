class Vehicle():
    '''транспортное средство'''

    def __init__(self, name, milage):
        '''свойства ТС'''
        self.name = name
        self.milage = milage

    def get_vehicle_type(self, wheels):
        '''возвращаем тип(колёсность) ТС'''
        vehicle_type = {2: 'мотоцикл', 3: 'трицикл', 4: 'автомобиль'}
        if wheels in vehicle_type:
            return print(f'Это {vehicle_type[wheels]} марки {self.name}')
        return print('Я не знаю таких ТС')

    def get_vehicle_advice(self):
        '''даём совет по покупке относительно пробега'''
        if self.milage < 50_001:
            return print(f'Неплохо, {self.name} можно брать')
        elif self.milage < 100_001:
            return print(f'{self.name} надо внимательно проверить')
        elif self.milage < 150_000:
            return print(f'{self.name} надо провести полную диагностику')
        return print(f'{self.name} лучше не покупать')


Vehicle_1 = Vehicle('Mercedes', 25_000)
Vehicle_2 = Vehicle('Lada', 75_000)
Vehicle_3 = Vehicle('KAMAZ', 130_000)
Vehicle_4 = Vehicle('Subaru', 200_000)

Vehicle_1.get_vehicle_type(2)
Vehicle_1.get_vehicle_advice()
print()
Vehicle_2.get_vehicle_type(1)
Vehicle_2.get_vehicle_advice()
print()
Vehicle_3.get_vehicle_type(4)
Vehicle_3.get_vehicle_advice()
print()
Vehicle_4.get_vehicle_type(3)
Vehicle_4.get_vehicle_advice()
print()


############################
class Education():
    '''Создаём класс по обучению'''

    def __init__(self, subject, teacher, textbook):
        self.subject = subject
        self.teacher = teacher
        self.textbook = textbook

    def get_teacher_and_subject(self):
        '''Узнаём какой учитель что преподаёт'''
        return print(f'Предмет "{self.subject}" преподаёт {self.teacher}')

    def get_grade(self, grade):
        '''Возвращаем мнение об успехах судя по оценки'''
        grade_dict = {
            1: 'тёмный лес',
            2: 'не лучший выбор',
            3: 'вполне подходит',
            4: 'правильное решение',
            5: 'лучший выбор'
        }
        if grade in grade_dict:
            return print(f'Для вас "{self.subject}" {grade_dict[grade]}')
        return print('Нет такой оценки')

    def get_textbook(self):
        '''рекомендация литературы по предмету'''
        return print(f'Для дальнейшего усвоения предмета {self.subject} вам поможет {self.textbook}')


educ_1 = Education('Математика', 'Валерий Палыч', 'Алгебра')
educ_2 = Education('Жизнь', 'Костян из 3-го подъезда', 'пачка Беломора')
educ_3 = Education('Физика', 'Эйнштейн', 'Теория Относительности')

educ_1.get_teacher_and_subject()
educ_1.get_grade(3)
educ_1.get_textbook()
print()
educ_2.get_teacher_and_subject()
educ_2.get_grade(1)
educ_2.get_textbook()
print()
educ_3.get_teacher_and_subject()
educ_3.get_grade(5)
educ_3.get_textbook()
print()
