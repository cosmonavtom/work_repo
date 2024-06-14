import pytest

from ..HW_25 import Teacher, DisciplineTeacher


@pytest.fixture
def teacher():
    teacher = Teacher('t_name', 't_education', 't_experience')
    return teacher


@pytest.fixture()
def dis_teacher():
    dis_teacher = DisciplineTeacher \
        ('t_name', 't_education', 't_experience', 't_discipline', 't_job_title')
    return dis_teacher
