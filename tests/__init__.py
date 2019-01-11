# -*- coding: utf-8 -*-
"""
    tests
    ~~~~~
    tests package
"""
from unittest import TestSuite, TextTestRunner, defaultTestLoader
from .api.journal_tests import JournalTestCase
from sqlalchemy import create_engine
from .settings import SESSION, SQLALCHEMY_DATABASE_URI 

class AppTestSuite(TestSuite):

    test_suite = defaultTestLoader.loadTestsFromTestCase(JournalTestCase)

    def __init__(self):
        super(AppTestSuite, self).__init__()
        self.addTest(self.test_suite)

def run_tests():
    # configure db connection
    engine = create_engine(SQLALCHEMY_DATABASE_URI)
    SESSION.configure(bind=engine)

    suite = AppTestSuite()
    runner = TextTestRunner()
    runner.run(suite)
