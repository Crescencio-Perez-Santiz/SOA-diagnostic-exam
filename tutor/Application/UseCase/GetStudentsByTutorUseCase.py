class GetStudentsByTutorUseCase:
    def __init__(self, tutor_repository, student_repository):
        self.tutor_repository = tutor_repository
        self.student_repository = student_repository

    def execute(self, tutor_name):
        tutor = self.tutor_repository.get_tutor_by_name(tutor_name)
        if tutor is None:
            return None
    
        students = [self._convert_student_to_dict(self.student_repository.get_student_by_enrolment(enrolment)) for enrolment in tutor["students"]]
        return students

    @staticmethod
    def _convert_student_to_dict(student):
        return {
            "student_name": student["student_name"],
            "enrolment": student["enrolment"],
            "contact": {
                "address": student["contact"]["address"],
                "email": student["contact"]["email"],
                "phone_number": student["contact"]["phone_number"]
            },
            "subjects": student["subjects"]
        }