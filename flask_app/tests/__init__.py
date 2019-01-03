# -*- coding: utf-8 -*-
"""
    tests
    ~~~~~
    tests package
"""
from unittest import TestSuite, TextTestRunner, defaultTestLoader
from tests.api.journal_tests import JournalTestCase

class AppTestSuite(TestSuite):

    test_cases = JournalTestCase()

    def __init__(self):
        super(AppTestSuite, self).__init__()
        self.addTest(self.test_cases)

# need to add code to configure scoped_session
if __name__ == '__main__':
    suite = AppTestSuite()
    runner = AppTestRunner()
    runner.run(suite)
