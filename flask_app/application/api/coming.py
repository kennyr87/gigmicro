from flask import Blueprint, render_template

coming = Blueprint('coming', __name__)

@coming.route('/')
def page():
    return render_template('coming.html')
