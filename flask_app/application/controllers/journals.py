from flask import Blueprint, request
from application.core import JournalService, FormError
from application.forms import JournalForm
from . import route

bp          = Blueprint('journals', __name__, url_prefix='/journals')
_journals   = JournalService()

@route(bp, '/')
def list_journals():
    """
    Returns a list of all journal instances

    :return: All journal instances
    :rtype: dict
    """
    j = _journals.all()
    return j.to_json()

@route(bp, '/<journal_id>')
def get_journal():
    """
    Returns a journal instance.

    :return: Journal instance
    :rtype: dict
    """
    j = _journals.get_or_404(journal_id)
    return j.to_json()

@route(bp, '/', methods=['POST'])
def add_journal():
    """
    Creates a new journal.

    :return: New journal instance
    :rtype: dict
    """
    form    = JournalForm()

    if form.validate_on_submit():
        j = _journals.create(**request.json)
        return j.to_json()
    raise FormError(form.errors)

@route(bp, '/<journal_id>', methods=['PUT'])
def update_journal():
    """
    Updates a journal entry

    :return: Instance of Journal
    :rtype: dict
    """
    form    = JournalForm()

    if form.validate_on_submit():
        j   = _journals.get_or_404(journal_id)
        j   = _journals.update(j, **request.json)
        return j.to_json()
    raise FormError(form.errors)

@route(bp, '<journal_id>', methods=['DELETE'])
def delete_journal():
    """
    Deletes a journal entry.

    :return: A 204 response.
    :rtype: tuple
    """
    j   = _journals.get_or_404(journal_id)
    _journals.delete(j)
    return None, 204
