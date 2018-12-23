from flask import Blueprint, render_template
from application.forms import JournalForm

bp = Blueprint('forms', __name__, url_prefix='/forms')

@bp.route('/journal')
def journal_form():
    form    = JournalForm()
    return render_template('forms/journal.html', form=form)
