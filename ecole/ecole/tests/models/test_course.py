from unittest.mock import Mock
import pytest
from datetime import date
from models.course import Course
def test_set_teacher():
    """Test setting a teacher to a course using a mock Teacher instance.

    This test checks that the course's teacher is correctly set to the mock Teacher instance,
    and ensures that the course appears in the teacher's list of courses taught.
    """

    course = Course(name="Physics", start_date=date(2024, 1, 1), end_date=date(2024, 6, 1))

    teacher_mock = Mock()
    teacher_mock.courses_teached = []

    course.set_teacher(teacher_mock)


    assert course.teacher == teacher_mock
    assert course in teacher_mock.courses_teached


def test_add_student():
    """Test adding a student to a course using a mock Student instance.

    This test verifies that the student is correctly added to the course's list of students
    and that the course is added to the student's list of courses taken.
    """


    course = Course(name="Mathematics", start_date=date(2024, 1, 1), end_date=date(2024, 6, 1))
    student_mock = Mock()
    student_mock.courses_taken = []

    course.add_student(student_mock)


    assert student_mock in course.students_taking_it
    assert course in student_mock.courses_taken