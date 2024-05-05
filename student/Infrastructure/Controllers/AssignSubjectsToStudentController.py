from flask import Blueprint, jsonify, request
from student.Application.UseCase.AssignSubjectsToStudentUseCase import AssignSubjectsToStudentUseCase

assign_subjects_to_student_blueprint = Blueprint('assign_subjects_to_student', __name__)

def initialize_endpoints(student_repository):
    assign_subjects_to_student_use_case = AssignSubjectsToStudentUseCase(student_repository)

    @assign_subjects_to_student_blueprint.route('/<enrolment>/subjects', methods=['PUT'])
    def assign_subjects_to_student(enrolment):
        subjects = request.json.get('subjects', [])
        student = assign_subjects_to_student_use_case.execute(enrolment, subjects)
        if student is not None:
            response = {
                "student_name": student['student_name'],
                "enrolment": enrolment,
                "subjects": student['subjects']
            }
            return jsonify(response), 200
        else:
            return jsonify({"error": "Student not found"}), 404