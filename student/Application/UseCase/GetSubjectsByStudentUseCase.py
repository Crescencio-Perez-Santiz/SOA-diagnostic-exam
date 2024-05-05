class GetSubjectsByStudentUseCase:
    def __init__(self, student_repository):
        self.student_repository = student_repository

    def execute(self, enrolment):
        
        student = self.student_repository.get_student_by_enrolment(enrolment)
        return student