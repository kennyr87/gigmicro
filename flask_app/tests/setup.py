# -*- coding: utf-8 -*-
"""
    tests.setup
    ~~~~~
    test setup environment
"""
from application import create_app
from unittest import TestCase, TextTestRunner
from tests.helpers import FlaskTestCaseMixin
from tests import Session
from tests.settings import SQLALCHEMY_DATABASE_URI
from sqlalchemy import create_engine

class AppTestRunner(TextTestRunner):
    """Basic text test runner implementation.

    """
    def __init__(self):
        """Configure SQLAlchemy session on start.

        """
        super(AppTestRunner, self).__init__()
        engine = create_engine(SQLALCHEMY_DATABASE_URI)
        Session.configure(bind=engine)

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

        # setup Flask request context
        self.app = self._create_app()
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()
        self._create_fixtures()
        self._create_csrf_token()

        # setup SQL Alchemy session for factories
        self.session = Session()

    def tearDown(self):
        super(AppTestCase, self).tearDown()

        # remove Flask request context
        self.app_context.pop()

        # remove SQL Alchemy session
        self.session.rollback()
        self.session.close()