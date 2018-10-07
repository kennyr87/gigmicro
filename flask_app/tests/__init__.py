"""
    tests
    ~~~~~
    tests package
"""
from unittest import TestSuite, TextTestRunner
from tests.journal_tests import JournalTestCase

class AppTestSuite(TestSuite):

    test_cases = (JournalTestCase())

    def __init__(self):
        super(TestSuite, self).__init__()
        self.addTest(test_cases)

if __name__ == '__main__':
    suite = AppTestSuite()
    runner = unittest.TextTestRunner()
    runner.run(suite)
