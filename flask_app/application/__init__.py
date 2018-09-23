from flask import Flask
from application.controllers import main, forms
from settings import app_config
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app(config_name):

    app = Flask('flask_app', template_folder='/srv/www/flask_app/templates')
    # initialize configuration
    app.config.from_object(app_config[config_name])
    # initialize database
    db.init_app(app)
    # register our blueprints
    app.register_blueprint(main.bp)
    app.register_blueprint(forms.bp)
    return app
