from flask import Flask
from application.controllers.app import main

def create_app( object_name ):

    app = Flask('flask_app', template_folder='/srv/www/flask_app/templates')
    app.config.from_object(object_name)

    # register our blueprints
    app.register_blueprint(main)
    return app
