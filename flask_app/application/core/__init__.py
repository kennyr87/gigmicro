# -*- coding: utf-8 -*-
"""
    flask_app.application.core
    ~~~~~
    core module
"""

from .core import Service
from .. import models

class AppError(Exception):
    """Base application error class."""

    def __init__(self, msg):
        self.msg = msg

class FormError(Exception):
    """Raise when an error processing a form occurs."""

    def __init__(self, errors=None):
        self.errors = errors

class URLService(Service):
    __model__       = models.ArticleURL

class ArticleService(Service):
    """
    Interface to Article Model
    """
    __model__       = models.Article

    def __init__(self):
        super().__init__()
        self.article_url    = URLService()

class AuthorService(Service):
    """
    Interface to Author model
    """
    __model__       = models.Author

class JournalService(Service):
    """
    Interface to Journal model
    """
    __model__       = models.Journal
