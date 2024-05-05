from flask import Blueprint, request, jsonify
from subject.Domain.Entity.Subject import Subject
from subject.Application.UseCase.CreateSubjectUseCase import CreateSubjectUseCase

subject_blueprint = Blueprint('subject', __name__)

def initialize_endpoints(repository):
    create_subject_use_case = CreateSubjectUseCase(repository)

    @subject_blueprint.route('/', methods=['POST'])
    def create_subject():
        try:
            subject_data = request.get_json()
            success, subject = create_subject_use_case.execute(Subject(**subject_data))
            
            if success:
                return jsonify({"message": "Subject created", "subject": subject}), 200
            else:
                return jsonify({"message": "Error creating subject", "error": subject}), 400
        except Exception as e:
            return jsonify({"message": "Error creating subject", "error": str(e)}), 400