# -*- coding: utf-8 -*-
"""
    tests
    ~~~~~
    tests package
"""
from unittest import TestSuite, TextTestRunner, defaultTestLoader
from .journal_tests import JournalTestCase
from sqlalchemy.orm import scoped_session, sessionmaker

Session = scoped_session(sessionmaker())

class AppTestSuite(TestSuite):

    test_cases = JournalTestCase()

    def __init__(self):
        super(AppTestSuite, self).__init__()
        self.addTest(self.test_cases)

# need to add code to configure scoped_session
if __name__ == '__main__':
    suite = AppTestSuite()
    runner = TextTestRunner()
    runner.run(suite)
