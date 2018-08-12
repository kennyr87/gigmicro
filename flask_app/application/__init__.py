from flask import Flask
from application.controllers.main import main
from flask_app.settings import app_config

def create_app(config_name):

    app = Flask('flask_app', template_folder='/srv/www/flask_app/templates')
    app.config.from_object(app_config[config_name])

    # register our blueprints
    app.register_blueprint(main)
    return app
