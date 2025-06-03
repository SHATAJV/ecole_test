# -*- coding: utf-8 -*-

"""
Classe Course
"""

from __future__ import annotations

from typing import Optional, TYPE_CHECKING
from dataclasses import dataclass, field
from datetime import date

if TYPE_CHECKING:
    from .student import Student
    from .teacher import Teacher


@dataclass
class Course:
    """Cours enseigné à l'école :
    - name               : nom du cours
    - start_date         : date de début
    - end_date           : date de fin
    - teacher            : enseignant de ce cours
    - students_taking_it : élèves qui suivent ce cours
    """
    name: str
    start_date: date
    end_date: date
    teacher: Optional[Teacher] = field(default=None, init=False)
    students_taking_it: list[Student] = field(default_factory=list, init=False)

    def set_teacher(self, teacher: Teacher) -> None:
        """Affecte un enseignant au cours, en gérant les éventuels remplacements."""
        if teacher != self.teacher:
            if self.teacher is not None:
                self.teacher.courses_teached.remove(self)
            teacher.courses_teached.append(self)
            self.teacher = teacher

    def add_student(self, student: Student) -> None:
        """Ajoute l'étudiant au cours, et le cours à l'étudiant."""
        self.students_taking_it.append(student)
        student.courses_taken.append(self)

    def __str__(self) -> str:
        base = f"{self.name} ({self.start_date} – {self.end_date})"
        return f"{base}, enseigné par {self.teacher}" if self.teacher else f"{base}, pas d'enseignant affecté"
