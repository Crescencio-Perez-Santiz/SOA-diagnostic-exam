from flask import Blueprint, jsonify
from student.Application.UseCase.GetSubjectsByStudentUseCase import GetSubjectsByStudentUseCase
from student.Infrastructure.Repository.StudentRepository import StudentRepository

get_subjects_by_student_blueprint = Blueprint('get_subjects_by_student', __name__)

def initialize_endpoints(student_repository: StudentRepository):
    get_subjects_by_student_use_case = GetSubjectsByStudentUseCase(student_repository)

    @get_subjects_by_student_blueprint.route('/<enrolment>/subjects', methods=['GET'])
    def get_subjects_by_student(enrolment):
        student = get_subjects_by_student_use_case.execute(enrolment)
        if student is not None:
            response = {
                "student_name": student['student_name'],
                "enrolment": enrolment,
                "subjects": student['subjects']
            }
            return jsonify(response), 200
        else:
            return jsonify({"error": "Student not found"}), 404