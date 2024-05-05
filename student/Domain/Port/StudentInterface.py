from abc import ABC, abstractmethod
from student.Domain.Entity.Student import Student

class StudentInterface(ABC):

    @abstractmethod
    def get_all_students(self):
        pass

    @abstractmethod
    def create_student(self, student: Student):
        pass

    @abstractmethod
    def assign_subjects_to_student(self, enrolment, subjects):
        pass