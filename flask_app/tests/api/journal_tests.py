"""
    tests.journal_tests
    ~~~~~~~~~~~~~~~~~~~~~~~
    journal tests module
"""

from .setup import AppTestCase
from application.models import Journal

class JournalTestCase(AppTestCase):

    """Fixture and test cases for journals api.

    Attributes:
        journal (:obj:`Journal`): Model for journal tables

    """
    def _create_fixtures(self):
        super(JournalTestCase, self)._create_fixtures()
        self.journal = Journal

    def test_get_journals(self):
        r = self.jget('/journals')
        self.assertOkJson(r)

    def test_get_journal(self):
        r = self.jget('/journals/%s' % self.journal.journal_id)
        self.assertOkJson(r)
