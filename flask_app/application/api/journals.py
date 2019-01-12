"""
    application.api.journals
    ~~~~~
    journals endpoints
"""

from flask import Blueprint, request
from ..core import JournalService, FormError
from ..forms import JournalForm
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
    return _journals.all()

@route(bp, '/<journal_id>')
def get_journal(journal_id):
    """
    Returns a journal instance.

    :return: Journal instance
    :rtype: dict
    """
    return _journals.get_or_404(journal_id)

@route(bp, '/', methods=['POST'])
def add_journal():
    """
    Creates a new journal.

    :return: New journal instance
    :rtype: dict
    """
    form    = JournalForm()

    if form.validate_on_submit():
        return _journals.create(**request.json)
    raise FormError(form.errors)

@route(bp, '/<journal_id>', methods=['PUT'])
def update_journal(journal_id):
    """
    Updates a journal entry

    :return: Instance of Journal
    :rtype: dict
    """
    form    = JournalForm()

    if form.validate_on_submit():
        j   = _journals.get_or_404(journal_id)
        j   = _journals.update(j, **request.json)
        return j
    raise FormError(form.errors)

@route(bp, '<journal_id>', methods=['DELETE'])
def delete_journal(journal_id):
    """
    Deletes a journal entry.

    :return: A 204 response.
    :rtype: tuple
    """
    j   = _journals.get_or_404(journal_id)
    _journals.delete(j)
    return None, 204
