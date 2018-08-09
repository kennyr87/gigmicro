from flask import Flask

from flask_app.application.app import main

def create_app( object_name ):

    app = Flask(__name__)

    app.config.from_object(object_name)

    # register our blueprints
    app.register_blueprint(main)

    return app
