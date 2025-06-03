import pytest
from models.student import Student


@pytest.mark.parametrize(
    "first_name, last_name, age, expected_student_nbr",
    [
        ("Alice", "Martin", 20, 1),
        ("Bob", "Durand", 22, 2),
        ("Charlie", "Petit", 19, 3),
    ],
)
def test_student_initialization(
    first_name, last_name, age, expected_student_nbr
):
    student = Student(
        first_name=first_name,
        last_name=last_name,
        age=age
    )
    assert student.first_name == first_name
    assert student.last_name == last_name
    assert student.age == age
    assert student.student_nbr == expected_student_nbr


