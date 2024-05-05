from flask import Blueprint, request, jsonify
from tutor.Domain.Entity.Tutor import Tutor
from tutor.Application.UseCase.CreateTutorUseCase import CreateTutorUseCase

tutor_blueprint = Blueprint('tutor', __name__)

def initialize_endpoints( tutor_repository, student_repository):
    create_tutor_use_case = CreateTutorUseCase(tutor_repository, student_repository)

    @tutor_blueprint.route('/', methods=['POST'])
    def create_tutor():
        try:
            tutor_data = request.get_json()
            success, tutor_id = create_tutor_use_case.execute(Tutor(**tutor_data))
            
            if success:
                return jsonify({"message": "Tutor created", "tutor_id": tutor_id}), 200
            else:
                return jsonify({"message": "Error creating tutor", "error": tutor_id}), 400
        except Exception as e:
            return jsonify({"message": "Error creating tutor", "error": str(e)}), 400