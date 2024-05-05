# StudentRepository.py
from database.MongoDB import get_db_connection
from student.Domain.Entity.Student import Student
from student.Domain.Port.StudentInterface import StudentInterface

class StudentRepository(StudentInterface):
    def __init__(self):
        self.db = get_db_connection()
        self.collection = self.db['students']

    def get_all_students(self):
        students = self.collection.find()
        return students
    
    def get_subjects_by_student(self, student_name):
        student = self.collection.find_one({"student_name": student_name})
        return student["subjects"]
    
    def creat_subjects_by_student(self, student_name, subjects):
        student = self.collection.find_one({"student_name": student_name})
        student["subjects"] = subjects
        self.collection.update_one({"student_name": student_name}, {"$set": student})
        return student["subjects"]

    def create_student(self, student: Student):
        student_data = {
            "student": str(student.student),
            "student_name": student.student_name,
            "enrolment": student.enrolment,
            "contact": student.contact,
            "tutor_uuid": student.tutor_uuid,
            "subjects": student.subjects
        }
        result = self.collection.insert_one(student_data)
        return str(result.inserted_id)
    
    def get_student_by_name(self, student_name):
        student = self.collection.find_one({"student_name": student_name})
        return student
    
    def get_student_by_enrolment(self, enrolment):
        student = self.collection.find_one({"enrolment": int(enrolment)})
        return student
    
    def assign_subjects_to_student(self, enrolment, subjects):
        student = self.collection.find_one({"enrolment": int(enrolment)})
        if student is not None:
            student["subjects"] = subjects
            self.collection.update_one({"enrolment": int(enrolment)}, {"$set": student})
        return student
    