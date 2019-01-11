"""
    application.api.main
    ~~~~~
    main application endpoints
"""

from flask import Blueprint, render_template
from . import journals

bp = Blueprint('main', __name__)

@bp.route('/')
def home():
    journal = journals.list_journals()
    return render_template('index.html', **journal)
