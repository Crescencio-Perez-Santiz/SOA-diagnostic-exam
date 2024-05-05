class AssignStudentsToTutorUseCase:
    def __init__(self, tutor_repository, student_repository):
        self.tutor_repository = tutor_repository
        self.student_repository = student_repository

    def execute(self, tutor_name, students):
        tutor = self.tutor_repository.get_tutor_by_name(tutor_name)
        if tutor is None:
            return None

        for enrolment in students:
            existing_student = self.student_repository.get_student_by_enrolment(enrolment)
            if existing_student is None:
                return None

        self.tutor_repository.assign_students_to_tutor(tutor_name, students)
        tutor = self.tutor_repository.get_tutor_by_name(tutor_name)
        return self._convert_tutor_to_dict(tutor)

    @staticmethod
    def _convert_tutor_to_dict(tutor):
        return {
            "_id": str(tutor["_id"]),
            "tutor_name": tutor["tutor_name"],
            "students": tutor["students"]
        }