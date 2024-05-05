from student.Infrastructure.Controllers.CreateStudentController import student_blueprint, initialize_endpoints
from student.Infrastructure.Controllers.GetAllStudentsController import get_all_students_blueprint, initialize_endpoints as initialize_endpoints_get_all_students
from student.Infrastructure.Controllers.GetSubjectsByStudentController import get_subjects_by_student_blueprint, initialize_endpoints as initialize_endpoints_get_subjects_by_student
from student.Infrastructure.Controllers.AssignSubjectsToStudentController import assign_subjects_to_student_blueprint, initialize_endpoints as initialize_endpoints_assign_subjects_to_student

def initialize_app(app, student_repository, subject_repository):
    initialize_endpoints(student_repository, subject_repository)
    initialize_endpoints_get_all_students(student_repository)
    initialize_endpoints_get_subjects_by_student(student_repository)
    initialize_endpoints_assign_subjects_to_student(student_repository)
    
    app.register_blueprint(student_blueprint, url_prefix="/students")
    app.register_blueprint(get_all_students_blueprint, url_prefix="/students")
    app.register_blueprint(get_subjects_by_student_blueprint, url_prefix="/students")
    app.register_blueprint(assign_subjects_to_student_blueprint, url_prefix="/students")