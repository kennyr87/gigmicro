"""
    application
    ~~~~~
    main application package
"""
from flask import Flask, render_template
from .api import main, journals
from ..settings import app_config
from .models import db
from .helpers import JSONEncoder

def on_404(error):
    return render_template('errors/404.html', error=error), 404

def create_app(config_name):

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
    app.register_error_handler(404, on_404)
    return app
