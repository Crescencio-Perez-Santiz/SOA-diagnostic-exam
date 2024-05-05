from abc import ABC, abstractmethod
from subject.Domain.Entity.Subject import Subject

class SubjectInterface(ABC):
    @abstractmethod
    def get_all_students(self):
        pass

    @abstractmethod
    def create_subject(self, subject: Subject):
        pass

    @abstractmethod
    def get_by_name(self, name):
        pass