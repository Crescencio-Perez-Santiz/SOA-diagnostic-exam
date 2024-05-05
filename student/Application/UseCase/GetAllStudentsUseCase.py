class GetAllStudentsUseCase:
    def __init__(self, student_repository):
        self.student_repository = student_repository

    def execute(self):
        students = self.student_repository.get_all_students()
        # students = [student['student_name'] for student in students]
        students = list(students)
        return students