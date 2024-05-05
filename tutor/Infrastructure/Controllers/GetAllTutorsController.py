from flask import Blueprint, jsonify
from tutor.Application.UseCase.GetAllTutorsUseCase import GetAllTutorsUseCase

get_all_tutors_blueprint = Blueprint('get_tutors', __name__)

def initialize_endpoints(tutor_repository):
    get_all_tutors_use_case = GetAllTutorsUseCase(tutor_repository)

    @get_all_tutors_blueprint.route('/', methods=['GET'])
    def get_all_tutors():
        tutors = get_all_tutors_use_case.execute()
        return jsonify(tutors), 200