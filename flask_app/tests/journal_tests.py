"""
    tests.journal_tests
    ~~~~~~~~~~~~~~~~~~~~~~~
    journal tests module
"""

from ..factories import CategoryFactory, ProductFactory
from . import AppTestCase

class JournalTestCase(AppTestCase):

    def _create_fixtures(self):
        super(JournalTestCase, self)._create_fixtures()
        pass

    def test_get_journals(self):
        r = self.jget('/journals')
        self.assertOkJson(r)

    def test_get_journal(self):
        r = self.jget('/journals/%s' % self.product.id)
        self.assertOkJson(r)
