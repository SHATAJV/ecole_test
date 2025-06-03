# -*- coding: utf-8 -*-
"""
Unit testing of class Course
"""

from datetime import date
from models.course import Course


def test_set_teacher(mocker):
    """Test that setting a teacher assigns the teacher to the course
    and updates the teacher's course list."""
    course = Course(
        name="Physics",
        start_date=date(2024, 1, 1),
        end_date=date(2024, 6, 1)
    )
    teacher_mock = mocker.Mock()
    teacher_mock.courses_teached = []

    course.set_teacher(teacher_mock)

    assert course.teacher == teacher_mock
    assert course in teacher_mock.courses_teached


def test_add_student(mocker):
    """Test that adding a student assigns the course to the student
    and updates the course's student list."""
    course = Course(
        name="Mathematics",
        start_date=date(2024, 1, 1),
        end_date=date(2024, 6, 1)
    )
    student_mock = mocker.Mock()
    student_mock.courses_taken = []

    course.add_student(student_mock)

    assert student_mock in course.students_taking_it
    assert course in student_mock.courses_taken
