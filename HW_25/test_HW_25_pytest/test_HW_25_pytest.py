from ..HW_25 import Teacher, DisciplineTeacher


def test_01_teacher_init(teacher):
    # teacher = Teacher('t_name', 't_education', 't_experience')
    assert len(Teacher.teachers_list) == 1
    Teacher.teachers_list.clear()


def test_02_get_teacher_name(teacher):
    assert teacher.get_teach_name() == 't_name'


def test_03_get_teach_educ(teacher):
    assert teacher.get_teach_educ() == 't_education'


def test_04_get_teach_exp(teacher):
    assert teacher.get_teach_exp() == 't_experience'


def test_05_set_teach_exp(teacher):
    teacher.set_teach_exp(10)
    assert teacher.get_teach_exp() == 10
    teacher.set_teach_exp('t_experience')


def test_06_get_teacher_data(teacher):
    assert teacher.get_teacher_data() == \
           't_name, образование t_education, опыт работы t_experience года'


def test_07_add_mark(teacher):
    assert teacher.add_mark('t_student', 't_mark') == \
           't_name поставил оценку t_mark студенту t_student'


def test_08_remove_mark(teacher):
    assert teacher.remove_mark('t_student', 't_mark') == \
           't_name удалил оценку t_mark студенту t_student'


def test_09_give_a_consultation(teacher):
    assert teacher.give_a_consultation('t_stud_class') == \
           't_name провёл консультацию в классе t_stud_class'


def test_10_fire_teacher(teacher):
    assert teacher.fire_teacher() == 'Учитель t_name уволен'
    assert teacher.fire_teacher() == 'Такого учителя нет в базе'


def test_11_get_discipline(dis_teacher):
    assert dis_teacher.get_discipline() == 't_discipline'


def test_12_get_job_title(dis_teacher):
    assert dis_teacher.get_job_title() == 't_job_title'


def test_13_set_job_title(dis_teacher):
    dis_teacher.set_job_title('test_new_job')
    assert dis_teacher.get_job_title() == 'test_new_job'
    dis_teacher.set_job_title('t_job_title')


def test_14_get_teacher_data(dis_teacher):
    assert dis_teacher.get_teacher_data() == \
           't_name, образование t_education, опыт работы t_experience года/n Предмет ' 't_discipline, должность t_job_title'


def test_15_add_mark(dis_teacher):
    assert dis_teacher.add_mark('t_student', 't_mark') == \
           't_name поставил оценку t_mark студенту t_student\nПредмет: t_discipline'


def test_16_remove_mark(dis_teacher):
    assert dis_teacher.remove_mark('t_student', 't_mark') == \
           't_name удалил оценку t_mark студенту t_student\nПредмет: t_discipline'


def test_17_give_a_consultation(dis_teacher):
    assert dis_teacher.give_a_consultation('t_stud_class') == \
           't_name провёл консультацию в классе t_stud_class\nПо предмету t_discipline как t_job_title'

def test_05_set_teach_exp(teacher):
    teacher.set_teach_exp(10)
    assert teacher.get_teach_exp() == 10
