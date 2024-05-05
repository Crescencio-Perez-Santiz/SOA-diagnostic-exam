class GetAllTutorsUseCase:
    def __init__(self, tutor_repository):
        self.tutor_repository = tutor_repository

    def execute(self):
        tutors_cursor = self.tutor_repository.get_all_tutors()
        tutors = [self._convert_tutor_to_dict(tutor) for tutor in tutors_cursor]
        return tutors

    @staticmethod
    def _convert_tutor_to_dict(tutor):
        return {
            "tutor_uuid": tutor["tutor_uuid"],
            "tutor_name": tutor["tutor_name"],
            "students": tutor["students"]
        }