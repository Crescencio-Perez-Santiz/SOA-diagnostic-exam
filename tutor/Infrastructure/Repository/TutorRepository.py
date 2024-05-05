from database.MongoDB import get_db_connection
from tutor.Domain.Port.TutorInterface import TutorInterface
from tutor.Domain.Entity.Tutor import Tutor

class TutorRepository(TutorInterface):
    def __init__(self):
        self.db = get_db_connection()
        self.collection = self.db['tutors']
        
    def get_all_tutors(self):
        tutors = self.collection.find()
        return tutors
    
    def create_tutor(self, tutor: Tutor):
        tutor_data = {
            "tutor_uuid": str(tutor.tutor_uuid),
            "tutor_name": tutor.tutor_name,
            "students": tutor.students
        }
        result = self.collection.insert_one(tutor_data)
        return str(result.inserted_id)
    
    def get_students_by_tutor(self, tutor_name):
        return self.collection.find_one({"tutor_name": tutor_name})["students"]
    
    def assign_students_to_tutor(self, tutor_name, students):
        return self.collection.update_one({"tutor_name": tutor_name}, {"$set": {"students": students}})
    
    def get_tutor_by_name(self, tutor_name):
        return self.collection.find_one({"tutor_name": tutor_name})
    
    