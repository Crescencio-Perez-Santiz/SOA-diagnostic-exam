from tutor.Domain.Entity.Tutor import Tutor

class CreateTutorUseCase:
    def __init__(self, tutor_repository, student_repository):
        self.tutor_repository = tutor_repository
        self.student_repository = student_repository

    def execute(self, tutor: Tutor):
        existing_tutor = self.tutor_repository.get_tutor_by_name(tutor.tutor_name)
        if existing_tutor is not None:
            return False, f"Tutor {tutor.tutor_name} already exists"

        for enrolment in tutor.students:
            existing_student = self.student_repository.get_student_by_enrolment(enrolment)
            if existing_student is None:
                return False, f"Student with enrolment {enrolment} does not exist"

        tutor_id = self.tutor_repository.create_tutor(tutor)
        return True, tutor_id