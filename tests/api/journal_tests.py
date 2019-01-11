"""
    tests.api.journal_tests
    ~~~~~~~~~~~~~~~~~~~~~~~
    journal tests module
"""

from unittest import skip
from ..setup import AppTestCase
from ..factory import JournalFactory, ArticleFactory

class JournalTestCase(AppTestCase):

    """Fixture and test cases for journals api.

    Attributes:
        journal (:obj:`JournalFactory`): Journal test data

    """
    def _create_fixtures(self):
        super(JournalTestCase, self)._create_fixtures()
        self.journal = JournalFactory()

    @skip('skip test get journals')
    def test_get_journals(self):
        r = self.jget('/journals')
        self.assertOkJson(r)

    @skip('skip test get journal')
    def test_get_journal(self):
        r = self.jget('/journals/%s' % self.journal.journal_id)
        self.assertOkJson(r)

    def test_create_journal(self):
        r = self.jpost('/journals', data={
            'journal_name': self.journal.journal_name,
            'journal_url': self.journal.journal_url,
            'issn_print': self.journal.issn_print,
            'issn_online': self.journal.issn_online
        })
        self.assertOkJson(r)