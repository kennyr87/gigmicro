"""
    tests.setup
    ~~~~~
    test setup environment
"""
from application import create_app
from unittest import TestCase
from .helpers import FlaskTestCaseMixin

class AppTestCase(FlaskTestCaseMixin, TestCase):
    """Create shared fixtures for all test cases

    Attributes:
        app (:obj:``)
        client (:obj: ``): Flask test client
    """
    def _create_app(self):
        return create_app('test')

    def _create_fixtures(self):
        pass

    def setUp(self):
        super(AppTestCase, self).setUp()
        self.app = self._create_app()
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()
        self._create_fixtures()
        self._create_csrf_token()

    def tearDown(self):
        super(AppTestCase, self).tearDown()
        self.app_context.pop()
