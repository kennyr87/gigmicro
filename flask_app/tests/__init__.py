"""
    tests
    ~~~~~
    tests package
"""
from unittest import TestSuite, TextTestRunner
from .journal_tests import JournalTestCase

class AppTestSuite(TestSuite):

    test_cases = JournalTestCase()

    def __init__(self):
        super(AppTestSuite, self).__init__()
        self.addTest(self.test_cases)

if __name__ == '__main__':
    suite = AppTestSuite()
    runner = TextTestRunner()
    runner.run(suite)
