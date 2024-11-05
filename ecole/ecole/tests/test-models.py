import pytest

from ecole.ecole.models.course import Course
from ecole.ecole.models.student import Student


@pytest.mark.parametrize("name, id, expected_student_nbr", [
    ("John", "12345", 1),
    ("Mark", "67890", 2),
    ("Antoine", "54321", 3)
])
def test_student_initialization(name, id, expected_student_nbr):
    student = Student(name, id)
    assert student.student_nbr == expected_student_nbr
    assert student.courses_taken == []
@pytest.mark.parametrize("course_name", ["Math", "Physics", "History"])
def test_add_course(course_name):
    student = Student("John", "12345")
    course = Course(course_name)
    student.add_course(course)
    assert course in student.courses_taken
    assert student in student.courses_taken