# -*- coding: utf-8 -*-
"""
    flask_app.factory
    ~~~~~
    application factory module
"""

from flask import Flask
from .settings import app_config
from .application.api import main, journals
from .application.models import db
from .helpers import JSONEncoder

def create_app(config_name):
    """
    Creates a Flask application

    """
    app = Flask('flask_app', template_folder='/srv/www/flask_app/templates')
    # initialize configuration
    app.config.from_object(app_config[config_name])
    # initialize database
    db.init_app(app)
    # Set the default JSON encoder
    app.json_encoder = JSONEncoder
    # register our blueprints
    app.register_blueprint(main.bp)
    app.register_blueprint(journals.bp)
    return app

