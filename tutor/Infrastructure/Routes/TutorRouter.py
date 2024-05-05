from tutor.Infrastructure.Controllers.CreateTutorController import  tutor_blueprint,initialize_endpoints as initialize_endpoints_tutor
from tutor.Infrastructure.Controllers.GetAllTutorsController import get_all_tutors_blueprint,initialize_endpoints as initialize_endpoints_get_all_tutors
from tutor.Infrastructure.Controllers.GetStudentsByTutorController import get_students_by_tutor_blueprint,  initialize_endpoints as initialize_endpoints_get_students_by_tutor
from tutor.Infrastructure.Controllers.AssignStudentsToTutorController import assign_students_to_tutor_blueprint, initialize_endpoints as initialize_endpoints_assign_students_to_tutor

def initialize_app(app, repository_tutor, repository_student):
    initialize_endpoints_tutor(repository_tutor, repository_student)
    initialize_endpoints_get_all_tutors(repository_tutor)
    initialize_endpoints_get_students_by_tutor(repository_tutor, repository_student)
    initialize_endpoints_assign_students_to_tutor(repository_tutor, repository_student)
    
    app.register_blueprint(tutor_blueprint, url_prefix="/api/v1/tutores")
    app.register_blueprint(get_all_tutors_blueprint, url_prefix="/api/v1/tutores")
    app.register_blueprint(get_students_by_tutor_blueprint, url_prefix="/api/v1/tutores")
    app.register_blueprint(assign_students_to_tutor_blueprint, url_prefix="/api/v1/tutores")