class Teacher:
    '''upd. Добавлен числовой счётчик инициации counter_init и приватный строчный счётчик
    __private_counter_init измеряющийся в звёздочках(*)'''
    teachers_list = []
    counter_init = 0
    __private_counter_init = ''

    def __init__(self, name, education, experience):
        self.__name = name
        self.__education = education
        self.__experience = experience
        self.teachers_list.append(self)
        Teacher.counter_init += 1
        Teacher.__private_counter_init += '*'

    @staticmethod
    def get_counter_init():
        '''Метод с помощью hasattr() проверяет наличие счётчика инициализации counter_init
        в Классе и при наличии возвращает его значение'''
        if hasattr(Teacher, 'counter_init'):
            return Teacher.counter_init
        else:
            return None

    def get_teach_name(self):
        return self.__name

    def get_teach_educ(self):
        return self.__education

    def get_teach_exp(self):
        return self.__experience

    def set_teach_exp(self, experience):
        self.__experience = experience

    def get_teacher_data(self):
        return f'{self.__name}, образование {self.__education}, опыт работы {self.__experience} года'

    def add_mark(self, student_name, mark):
        return f'{self.__name} поставил оценку {mark} студенту {student_name}'

    def remove_mark(self, student_name, mark):
        return f'{self.__name} удалил оценку {mark} студенту {student_name}'

    def give_a_consultation(self, stud_class):
        return f'{self.__name} провёл консультацию в классе {stud_class}'

    def fire_teacher(self):
        if self in self.teachers_list:
            fired = f'Учитель {self.__name} уволен'
            self.teachers_list.remove(self)
            return fired
        else:
            return 'Такого учителя нет в базе'


class DisciplineTeacher(Teacher):

    def __init__(self, name, education, experience, discipline, job_title):
        super().__init__(name, education, experience)
        self.__discipline = discipline
        self.__job_title = job_title

    def get_discipline(self):
        return self.__discipline

    def get_job_title(self):
        return self.__job_title

    def set_job_title(self, job_title):
        self.__job_title = job_title

    def get_teacher_data(self):
        return f'{super().get_teacher_data()}/n Предмет {self.__discipline}, должность {self.__job_title}'

    def add_mark(self, student_name, mark):
        return f'{super().add_mark(student_name, mark)}\nПредмет: {self.__discipline}'

    def remove_mark(self, student_name, mark):
        return f'{super().remove_mark(student_name, mark)}\nПредмет: {self.__discipline}'

    def give_a_consultation(self, stud_class):
        return f'{super().give_a_consultation(stud_class)}\nПо предмету {self.__discipline} как {self.__job_title}'


teacher_1 = Teacher('Андрей Андреевич', 'среднее', 11)
teacher_2 = Teacher('Борис Борисович', 'СПбГУ', 22)
teacher_2.set_teach_exp(23)
d_teacher_1 = DisciplineTeacher('Владимир Владимирович', 'ЛГУ', 33, 'Химия', 'Завуч')

print(Teacher.__doc__)
print(Teacher.__dict__)
print(teacher_1.__dict__, teacher_1.counter_init)
print(teacher_2.__dict__, teacher_2._Teacher__private_counter_init)
print(d_teacher_1.__dict__, d_teacher_1.counter_init)
print('Кол-во учителей:', d_teacher_1.get_counter_init())
print(f'Класс {Teacher.__name__} старался быть названным логично своему функционалу')
print(Teacher.__bases__, DisciplineTeacher.__bases__)