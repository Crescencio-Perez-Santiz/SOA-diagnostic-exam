from subject.Infrastructure.Controllers.CreateSubjectController import subject_blueprint, initialize_endpoints

def initialize_app(app, repository):
    initialize_endpoints(repository)
    app.register_blueprint(subject_blueprint, url_prefix="/subjects")