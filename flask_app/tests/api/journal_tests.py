"""
    tests.journal_tests
    ~~~~~~~~~~~~~~~~~~~~~~~
    journal tests module
"""

from tests.setup import AppTestCase
from tests.factory import JournalFactory, ArticleFactory

class JournalTestCase(AppTestCase):

    """Fixture and test cases for journals api.

    Attributes:
        journal (:obj:`JournalFactory`): Journal test data

    """
    def _create_fixtures(self):
        super(JournalTestCase, self)._create_fixtures()
        self.journal = JournalFactory()

    def test_get_journals(self):
        r = self.jget('/journals')
        self.assertOkJson(r)

    def test_get_journal(self):
        r = self.jget('/journals/%s' % self.journal.journal_id)
        self.assertOkJson(r)
