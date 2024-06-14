import unittest
from ..HW_25 import Teacher, DisciplineTeacher


class TestTeacher(unittest.TestCase):
    teacher = Teacher('t_name', 't_educ', 't_exp')

    def test_01_init(self):
        self.assertEqual(len(Teacher.teachers_list), 2)

    def test_02_get_teacher_name(self):
        self.assertEqual(self.teacher.get_teach_name(), 't_name')

    def test_03_get_teach_educ(self):
        self.assertEqual(self.teacher.get_teach_educ(), 't_educ')

    def test_04_get_teach_exp(self):
        self.assertEqual(self.teacher.get_teach_exp(), 't_exp')

    def test_05_set_teach_exp(self):
        self.teacher.set_teach_exp(10)
        self.assertEqual(self.teacher.get_teach_exp(), 10)
        self.teacher.set_teach_exp('t_exp')

    def test_06_get_teacher_data(self):
        self.assertEqual(self.teacher.get_teacher_data(), \
                         't_name, образование t_educ, опыт работы t_exp года')

    def test_07_add_mark(self):
        self.assertEqual(self.teacher.add_mark('t_student_name', 't_mark'), \
                         't_name поставил оценку t_mark студенту t_student_name')

    def test_08_remove_mark(self):
        self.assertEqual(self.teacher.remove_mark('t_student_name', 't_mark'), \
                         't_name удалил оценку t_mark студенту t_student_name')

    def test_09_give_a_consultation(self):
        self.assertEqual(self.teacher.give_a_consultation('t_stud_class'), \
                         't_name провёл консультацию в классе t_stud_class')

    def test_10_fire_teacher(self):
        self.assertEqual(self.teacher.fire_teacher(), 'Учитель t_name уволен')
        self.assertEqual(self.teacher.fire_teacher(), 'Такого учителя нет в базе')


class TestDisciplineTeacher(unittest.TestCase):
    dis_teacher = DisciplineTeacher('t_name', 't_educ', 't_exp', 't_discip', 't_jt')

    def test_11_get_discipline(self):
        self.assertEqual(self.dis_teacher.get_discipline(), 't_discip')

    def test_12_get_job_title(self):
        self.assertEqual(self.dis_teacher.get_job_title(), 't_jt')

    def test_13_set_job_title(self):
        self.dis_teacher.set_job_title('t_Director')
        self.assertEqual(self.dis_teacher.get_job_title(), 't_Director')
        self.dis_teacher.set_job_title('t_jt')

    def test_14_get_teacher_data(self):
        self.assertEqual(self.dis_teacher.get_teacher_data(), \
                         't_name, образование t_educ, опыт работы t_exp года/n Предмет t_discip, должность t_jt')

    def test_15_add_mark(self):
        self.assertEqual(self.dis_teacher.add_mark('t_stud_name', 't_mark'), \
                         't_name поставил оценку t_mark студенту t_stud_name\nПредмет: t_discip')

    def test_16_remove_mark(self):
        self.assertEqual(self.dis_teacher.remove_mark('t_stud_name', 't_mark'), \
                        't_name удалил оценку t_mark студенту t_stud_name\nПредмет: t_discip')

    def test_17_give_a_consultation(self):
        self.assertEqual(self.dis_teacher.give_a_consultation('t_stud_class'), \
                         't_name провёл консультацию в классе t_stud_class\nПо предмету t_discip как t_jt')