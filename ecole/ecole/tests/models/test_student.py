"""
Unit testing of class Student
"""
import pytest
from datetime import date
from models.student import Student

@pytest.mark.parametrize("first_name, last_name, age, expected_student_nbr", [
    ("John", "Smith", 10, 1),
    ("Mark", "Brown", 8, 2),
    ("Antoine", "Jane", 9, 3)
])
def test_student_initialization(first_name, last_name, age, expected_student_nbr):
    """Test the initialization of a Student instance.

    This test verifies that a Student object is correctly initialized with the given first name,
    last name, and age, and that the student number matches the expected value. It also checks
    that the student's list of courses taken is initially empty.

    Parameters:
    - first_name (str): The first name of the student.
    - last_name (str): The last name of the student.
    - age (int): The age of the student.
    - expected_student_nbr (int): The expected student number to be assigned upon initialization.
    """

    student = Student(first_name, last_name, age)
    assert student.student_nbr == expected_student_nbr
    assert student.courses_taken == []


@pytest.mark.parametrize("course_name", ["Math", "Physics", "History"])
def test_add_course(mocker, course_name):
    """Test adding a course to a Student's list of courses taken using mocks.

    This test verifies that when a course is added to a Student, it appears in the
    student's list of courses taken and the student is added to the course's list
    of students taking it, using mock objects for isolation.

    Parameters:
    - course_name (str): The name of the course to be added to the student's course list.
    """

    student = Student("John", "Smith", 10)

    # Use mocker to create a mock Course object
    course_mock = mocker.Mock()
    course_mock.name = course_name
    course_mock.students_taking_it = []

    student.add_course(course_mock)


    assert course_mock in student.courses_taken


    assert student in course_mock.students_taking_it


def test_student_str():
    """Test the string representation of Student instance."""
    student = Student("Jane", "Doe", 20)
    expected_str = f"{student.first_name} {student.last_name} ({student.age} ans), n° étudiant : {student.student_nbr}"
    assert str(student) == expected_str
