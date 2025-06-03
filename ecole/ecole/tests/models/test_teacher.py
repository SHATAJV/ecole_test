from datetime import date
from models.teacher import Teacher
from models.course import Course
from models.address import Address

def test_teacher_address():
    teacher = Teacher(
        first_name="Jane",
        last_name="Smith",
        age=35,
        hiring_date=date(2021, 5, 15),
    )

    address = Address(street="123 Main St", city="Paris", postal_code=75001)
    teacher.address = address

    assert teacher.address == address


def test_teacher_str():
    teacher = Teacher(
        first_name="Jane",
        last_name="Smith",
        age=35,
        hiring_date=date(2021, 5, 15),
    )
    address = Address(street="123 Main St", city="Paris", postal_code=75001)
    teacher.address = address

    expected_str = (
        "Jane Smith (35 ans), 123 Main St, 75001 Paris, "
        "arrivé(e) le 2021-05-15"
    )
    assert str(teacher) == expected_str

    teacher.address = None
    expected_str_no_address = "Jane Smith (35 ans), arrivé(e) le 2021-05-15"
    assert str(teacher) == expected_str_no_address

def test_teacher_add_course_with_mock(mocker):
    teacher = Teacher(
        first_name="Alice", last_name="Brown", age=45, hiring_date=date(2019, 8, 20)
    )

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
