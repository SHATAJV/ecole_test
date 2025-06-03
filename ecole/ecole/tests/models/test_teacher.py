# -*- coding: utf-8 -*-
"""
Unit testing of class Teacher
"""

from datetime import date
import pytest
from models.teacher import Teacher
from models.course import Course
from models.address import Address


def test_teacher_initialization():
    """Test initialization of a Teacher instance."""
    hiring_date = date(2020, 9, 1)
    teacher = Teacher(
        first_name="Didier", last_name="Decoin", age=36, hiring_date=hiring_date
    )

    assert teacher.first_name == "Didier"
    assert teacher.last_name == "Decoin"
    assert teacher.age == 36
    assert teacher.hiring_date == hiring_date
    assert teacher.courses_teached == []
    assert teacher.address is None


def test_teacher_address():
    """Test assigning an address to a Teacher."""
    teacher = Teacher(
        first_name="Jane", last_name="Smith", age=35, hiring_date=date(2021, 5, 15)
    )
    address = Address(street="123 Main St", city="Paris", postal_code=75001)
    teacher.address = address

    assert teacher.address == address


def test_teacher_str():
    """Test string representation of a Teacher."""
    teacher = Teacher(
        first_name="Jane", last_name="Smith", age=35, hiring_date=date(2021, 5, 15)
    )
    address = Address(street="123 Main St", city="Paris", postal_code=75001)
    teacher.address = address

    assert str(teacher) == (
        "Jane Smith (35 ans), 123 Main St, 75001 Paris, arrivé(e) le 2021-05-15"
    )

    teacher.address = None
    assert str(teacher) == "Jane Smith (35 ans), arrivé(e) le 2021-05-15"


def test_teacher_add_course_with_mock(mocker):
    """Test adding a mock course to a Teacher."""
    teacher = Teacher(
        first_name="Alice", last_name="Brown", age=45, hiring_date=date(2019, 8, 20)
    )
    course_mock = mocker.Mock()
    course_mock.name = "Mathematics"

    teacher.add_course(course_mock)

    assert course_mock.teacher == teacher
    assert course_mock in teacher.courses_teached


def test_add_course():
    """Test adding a real Course instance to a Teacher."""
    teacher = Teacher("Marc", "Durand", 40, date(2022, 1, 1))
    course = Course("Histoire", date(2022, 1, 10), date(2022, 6, 30))

    teacher.add_course(course)

    assert course in teacher.courses_teached
