from flask import Flask

from subject.Infrastructure.Repository.SubjectRepository import SubjectRepository
from student.Infrastructure.Repository.StudentRepository import StudentRepository
from tutor.Infrastructure.Repository.TutorRepository import TutorRepository
from tutor.Infrastructure.Routes.TutorRouter import initialize_app as initialize_app_tutor
from student.Infrastructure.Routes.StudentRouter import initialize_app as initialize_app_student
from subject.Infrastructure.Routes.SubjectRouter import initialize_app as initialize_app_subject

repository_subject = SubjectRepository()
respository_student = StudentRepository()
repository_tutor = TutorRepository()

app = Flask(__name__)

initialize_app_subject(app, repository_subject)
initialize_app_student(app, respository_student, repository_subject)
initialize_app_tutor(app, repository_tutor, respository_student)

if __name__ == "__main__":
    app.run(debug=True)
