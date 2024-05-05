from student.Domain.Entity.Student import Student

class CreateStudentUseCase:
    def __init__(self, student_repository, subject_repository):
        self.student_repository = student_repository
        self.subject_repository = subject_repository

    def execute(self, student: Student):
        existing_student_by_name = self.student_repository.get_student_by_name(student.student_name)
        if existing_student_by_name is not None:
            return False, f"Student {student.student_name} already exists"

        existing_student_by_enrolment = self.student_repository.get_student_by_enrolment(student.enrolment)
        if existing_student_by_enrolment is not None:
            return False, f"Student with enrolment {student.enrolment} already exists"

        for subject_name in student.subjects:
            subject = self.subject_repository.get_by_name(subject_name)
            if subject is None:
                return False, f"Subject {subject_name} does not exist"

        student_id = self.student_repository.create_student(student)
        return True, student_id