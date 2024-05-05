# StudentRepository.py
from database.MongoDB import get_db_connection
from subject.Domain.Entity.Subject import Subject
from subject.Domain.Port.SubjectInterface import SubjectInterface

class SubjectRepository(SubjectInterface):
    def __init__(self):
        self.db = get_db_connection()
        self.collection = self.db['subjects']

    def get_all_students(self):
        subjects = self.collection.find()
        return subjects

    def create_subject(self, subject: Subject):
        subject_data = {
            "subject_name": str(subject.subject_name),
        }
        result = self.collection.insert_one(subject_data)
        return result.inserted_id
    
    def get_by_name(self, name):
        subject = self.collection.find_one({"subject_name": name})
        return subject
    