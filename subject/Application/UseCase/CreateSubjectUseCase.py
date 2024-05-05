from subject.Domain.Entity.Subject import Subject as SubjectDomain

class CreateSubjectUseCase:
    def __init__(self, repository):
        self.repository = repository
        
    def execute(self, subject: SubjectDomain):
        name_exist = self.repository.get_by_name(subject.subject_name)
        if name_exist is not None:
            return False, {"error": "Subject already exists"}
        try:
            self.repository.create_subject(subject)
            return True, subject
        except Exception as e:
            return False, {"error": str(e)}