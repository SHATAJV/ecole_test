from datetime import date

from pytest_mock import mocker

from models.teacher import Teacher
from models.course import Course
from models.address import Address


def test_teacher_initialization():

    hiring_date = date(2020, 9, 1)
    teacher = Teacher(first_name="Didier", last_name="Decoin", age=36, hiring_date=hiring_date)

    assert teacher.first_name == "Didier"
    assert teacher.last_name == "Decoin"
    assert teacher.age == 36
    assert teacher.hiring_date == hiring_date
    assert teacher.courses_teached == []
    assert teacher.address is None


def test_teacher_address():


    teacher = Teacher(first_name="Jane", last_name="Smith", age=35, hiring_date=date(2021, 5, 15))

    address = Address(street="123 Main St", city="Paris", postal_code=75001)
    teacher.address = address

    assert teacher.address == address

def test_teacher_str():


    teacher = Teacher(first_name="Jane", last_name="Smith", age=35, hiring_date=date(2021, 5, 15))
    address = Address(street="123 Main St", city="Paris", postal_code=75001)
    teacher.address = address

    assert str(teacher) == "Jane Smith (35 ans), 123 Main St, 75001 Paris, arrivé(e) le 2021-05-15"

    teacher.address = None
    assert str(teacher) == "Jane Smith (35 ans), arrivé(e) le 2021-05-15"


def test_teacher_add_course_with_mock(mocker):
    teacher = Teacher(first_name="Alice", last_name="Brown", age=45, hiring_date=date(2019, 8, 20))

    course_mock = mocker.Mock()
    course_mock.name = "Mathematics"

    teacher.add_course(course_mock)

    assert course_mock.teacher == teacher
    assert course_mock in teacher.courses_teached


def test_add_course():
    teacher = Teacher("Marc", "Durand", 40, date(2022, 1, 1))
    course = Course("Histoire")

    teacher.add_course(course)

    assert course in teacher.courses_teached
