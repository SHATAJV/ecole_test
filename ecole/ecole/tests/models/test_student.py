import pytest
from models.student import Student


@pytest.mark.parametrize(
    "first_name, last_name, age, expected_student_nbr",
    [
        ("John", "Smith", 10, 1),
        ("Mark", "Brown", 8, 2),
        ("Antoine", "Jane", 9, 3),
    ],
)
def test_student_initialization(first_name, last_name, age, expected_student_nbr):
    student = Student(first_name, last_name, age)

    assert student.student_nbr == expected_student_nbr
    assert student.courses_taken == []


@pytest.mark.parametrize("course_name", ["Math", "Physics", "History"])
def test_add_course(mocker, course_name):
    student = Student("John", "Smith", 10)

    course_mock = mocker.Mock()
    course_mock.name = course_name
    course_mock.students_taking_it = []

    student.add_course(course_mock)

    assert course_mock in student.courses_taken
    assert student in course_mock.students_taking_it


def test_student_str():
    student = Student("Jane", "Doe", 20)
    expected_str = (
        f"{student.first_name} {student.last_name} "
        f"({student.age} ans), n° étudiant : {student.student_nbr}"
    )

    assert str(student) == expected_str
