# test_teacher.py


import pytest
from datetime import date

from pytest_mock import mocker

from models.teacher import Teacher
from models.course import Course
from models.address import Address


def test_teacher_initialization():
    """Test the initialization of a Teacher instance with inherited attributes from Person.

    This test verifies that a Teacher object is correctly initialized with the given first name,
    last name, age, hiring date, and that it starts with an empty list of courses taught and no address.
    """

    hiring_date = date(2020, 9, 1)
    teacher = Teacher(first_name="Didier", last_name="Decoin", age=36, hiring_date=hiring_date)

    assert teacher.first_name == "Didier"
    assert teacher.last_name == "Decoin"
    assert teacher.age == 36
    assert teacher.hiring_date == hiring_date
    assert teacher.courses_teached == []
    assert teacher.address is None


def test_teacher_address():
    """Test the assignment of an address to a Teacher instance.

    This test checks that a Teacher's address can be set and retrieved correctly.
    It creates an Address object and assigns it to the Teacher, then verifies that the address
    attribute reflects this assignment.
    """

    teacher = Teacher(first_name="Jane", last_name="Smith", age=35, hiring_date=date(2021, 5, 15))

    address = Address(street="123 Main St", city="Paris", postal_code=75001)
    teacher.address = address

    assert teacher.address == address



def test_teacher_str():
    """Test the string representation of a Teacher instance.

    This test verifies that the string representation of a Teacher object accurately reflects its
    attributes. It checks the output when the Teacher has an address assigned and when no address
    is assigned, ensuring the format is consistent with expected output.
    """

    teacher = Teacher(first_name="Jane", last_name="Smith", age=35, hiring_date=date(2021, 5, 15))
    address = Address(street="123 Main St", city="Paris", postal_code=75001)
    teacher.address = address

    assert str(teacher) == "Jane Smith (35 ans), 123 Main St, 75001 Paris, arrivé(e) le 2021-05-15"

    teacher.address = None
    assert str(teacher) == "Jane Smith (35 ans), arrivé(e) le 2021-05-15"


def test_teacher_add_course_with_mock(mocker):
    """Test adding a course to a Teacher's list using a mock Course instance.

    This test ensures that when a mock course is added to a Teacher's list of courses taught,
    the course's teacher attribute is correctly assigned to the Teacher instance and that
    the course appears in the Teacher's courses_teached list.
    """

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



