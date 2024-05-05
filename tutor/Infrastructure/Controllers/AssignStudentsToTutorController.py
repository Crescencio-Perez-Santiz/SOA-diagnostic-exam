from flask import Blueprint, jsonify, request
from tutor.Application.UseCase.AssignStudentsToTutorUseCase import AssignStudentsToTutorUseCase

assign_students_to_tutor_blueprint = Blueprint('assign_students_to_tutor', __name__)

def initialize_endpoints(tutor_repository, student_repository):
    assign_students_to_tutor_use_case = AssignStudentsToTutorUseCase(tutor_repository, student_repository)

    @assign_students_to_tutor_blueprint.route('/<tutor_name>/students', methods=['PUT'])
    def assign_students_to_tutor(tutor_name):
        students = request.json.get('students', [])
        tutor = assign_students_to_tutor_use_case.execute(tutor_name, students)
        if tutor is not None:
            return jsonify(tutor), 200
        else:
            return jsonify({"error": "Tutor or students not found"}), 404