"""
    tests.journal_tests
    ~~~~~~~~~~~~~~~~~~~~~~~
    journal tests module
"""

from .setup import AppTestCase
from application.models import Journal

class JournalTestCase(AppTestCase):

    def _create_fixtures(self):
        super(JournalTestCase, self)._create_fixtures()
        j = Journal.query.get(1)
        self.journal = j

    def test_get_journals(self):
        r = self.jget('/journals')
        self.assertOkJson(r)

    def test_get_journal(self):
        r = self.jget('/journals/%s' % self.journal.journal_id)
        self.assertOkJson(r)
