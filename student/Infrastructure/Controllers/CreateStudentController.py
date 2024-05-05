from flask import Blueprint, request, jsonify
from student.Domain.Entity.Student import Student
from student.Application.UseCase.CreateStudentUseCase import CreateStudentUseCase
from subject.Infrastructure.Repository.SubjectRepository import SubjectRepository


student_blueprint = Blueprint('student', __name__)

def initialize_endpoints(student_repository, subject_repository: SubjectRepository):
    create_student_use_case = CreateStudentUseCase(student_repository, subject_repository)

    @student_blueprint.route('/', methods=['POST'])
    def create_student():
        try:
            student_data = request.get_json()
            success, student = create_student_use_case.execute(Student(**student_data))
            if success:
                return jsonify({"message": "Student created", "student": student}), 200
            else:
                return jsonify({"message": "Error creating student", "error": student}), 400
        except Exception as e:
            return jsonify({"message": "Error creating student", "error": str(e)}), 400