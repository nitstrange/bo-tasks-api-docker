# services/users/project/__init__.py


import os
import project.config
from flask import Flask  # new
from flask_sqlalchemy import SQLAlchemy


# instantiate the db
db = SQLAlchemy()


# new
def create_app(script_info=None):

    # instantiate the app
    app = Flask(__name__)

    # set config
    #change the line here if you running application on docker
    app_settings = project.config.DevelopmentConfig #os.getenv('APP_SETTINGS')
    
    app.config.from_object(app_settings)
    
    # set up extensions
    db.init_app(app)

    # register blueprints
    from project.api.tasks import tasks_blueprint

    app.register_blueprint(tasks_blueprint)

    # shell context for flask cli
    @app.shell_context_processor
    def ctx():
        return {'app': app, 'db': db}

    return app
