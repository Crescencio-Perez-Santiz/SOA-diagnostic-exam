from flask import Blueprint, jsonify
from tutor.Application.UseCase.GetStudentsByTutorUseCase import GetStudentsByTutorUseCase

get_students_by_tutor_blueprint = Blueprint('get_students_by_tutor', __name__)

def initialize_endpoints(tutor_repository, student_repository):
    get_students_by_tutor_use_case = GetStudentsByTutorUseCase(tutor_repository, student_repository)

    @get_students_by_tutor_blueprint.route('/<tutor_name>/students', methods=['GET'])
    def get_students_by_tutor(tutor_name):
        students = get_students_by_tutor_use_case.execute(tutor_name)
        if students is not None:
            return jsonify(students), 200
        else:
            return jsonify({"error": "Tutor not found"}), 404