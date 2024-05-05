from flask import Blueprint, jsonify
from bson import json_util
import json
from student.Application.UseCase.GetAllStudentsUseCase import GetAllStudentsUseCase

get_all_students_blueprint = Blueprint('get_all_students', __name__)

def initialize_endpoints(student_repository):
    get_all_students_use_case = GetAllStudentsUseCase(student_repository)

    @get_all_students_blueprint.route('/', methods=['GET'])
    def get_all_students():
        students = get_all_students_use_case.execute()
        students = [json.loads(json_util.dumps(student)) for student in students]
        return jsonify({"student_names": students}), 200