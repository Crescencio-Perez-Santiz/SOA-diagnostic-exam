from abc import ABC, abstractmethod

class TutorInterface(ABC):
    
    @abstractmethod
    def get_all_tutors(self):
        pass
    
    @abstractmethod
    def create_tutor(self, tutor):
        pass
    
    @abstractmethod
    def get_students_by_tutor(self, tutor_name):
        pass
    
    @abstractmethod
    def assign_students_to_tutor(self, tutor_name, students):
        pass