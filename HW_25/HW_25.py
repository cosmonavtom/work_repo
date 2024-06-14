class Teacher:
    teachers_list = []

    def __init__(self, name, education, experience):
        self.__name = name
        self.__education = education
        self.__experience = experience
        self.teachers_list.append(self)

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

# if __name__ == '__main__':
#     Teacher_1 = Teacher('Иван Иванович', 'среднее', 22)
#     Teacher_1.set_teach_exp(23)
#     print(Teacher_1.get_teacher_data())
#     print(Teacher_1.add_mark('Петя Петров', 5))
#     print(Teacher_1.remove_mark('Настя Фролова', 3))
#     print(Teacher_1.give_a_consultation('5-A'))
#     print()
#
#     Teacher_2 = DisciplineTeacher('Сергей Сергеевич', 'МГУ', 33, 'Химия', 'Завуч')
#     Teacher_2.set_job_title('Директор')
#     print(Teacher_2.get_teacher_data())
#     print(Teacher_2.add_mark('Костя Костин', 4))
#     print(Teacher_2.remove_mark('Саша Сашин', 5))
#     print(Teacher_2.give_a_consultation('4-Б'))
#     print(len(Teacher.teachers_list))
#     print(Teacher_1.fire_teacher())
#     print(Teacher_1.fire_teacher())
#     print(len(Teacher.teachers_list))

