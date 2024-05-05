class AssignSubjectsToStudentUseCase:
    def __init__(self, student_repository):
        self.student_repository = student_repository

    def execute(self, enrolment, subjects):
        student = self.student_repository.assign_subjects_to_student(enrolment, subjects)
        return student