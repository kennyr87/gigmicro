from core import JournalService, FormError
from application.forms import JournalForm

bp          = Blueprint('journals', __name__, url_prefix='/journals')
_journals   = JournalService()

@bp.route('/')
def list_journals():
    """
    Returns a list of all journal instances
    """
    return _journals.all()

@bp.route('/<journal_id>'):
def get_journal():
    """
    Returns a journal instance.

    :return: Instance of Journal
    """
    return _journals.get_or_404(journal_id)

@bp.route('/', method=['POST'])
def add_journal():
    """
    Creates a new journal.

    :return: Instance of Journal.
    """
    form    = JournalForm()

    if form.validate_on_submit():
        return _journals.create(**request.json)
    raise FormError(form.errors)

@bp.route('/<journal_id>', method=['PUT']):
def update_journal():
    """
    Updates a journal entry

    :return: Instance of Journal
    """
    form    = JournalForm()

    if form.validate_on_submit():
        j   = _journals.get_or_404(journal_id)
        return _journals.update(j, **request.json)
    raise FormError(form.errors)

@bp.route('<journal_id>', method=['DELETE']):
def delete_journal():
    """
    Deletes a journal entry.

    :return: A 204 response.
    :rtype: tuple
    """
    j   = _journals.get_or_404(journal_id)
    _journals.delete(j)

    return None, 204
