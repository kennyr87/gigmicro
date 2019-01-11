# -*- coding: utf-8 -*-
"""
    tests.factory
    ~~~~~~~~~~~~~~~

    Factories for test fixture data
"""

from factory import SubFactory, Faker, alchemy, sequence
from flask_app.application.models import Journal, Article, Author, ArticleURL
from .settings import SESSION

class AppFactory(object):
    sqlalchemy_session              = SESSION
    sqlalchemy_session_persistence  = 'commit'

class JournalFactory(alchemy.SQLAlchemyModelFactory):
    class Meta(AppFactory):
        model       = Journal

    @sequence
    def journal_id(n):
        """Add integer to counter to avoid duplicate id error.

        """
        id = n + 2
        return '%d' % id

    journal_name    = Faker('bs')
    journal_url     = Faker('url')
    issn_print      = Faker('ean', length=8)
    issn_online     = Faker('ean', length=8)

class ArticleFactory(alchemy.SQLAlchemyModelFactory):
    class Meta(AppFactory):
        model       = Article

    article_name    = Faker('text', max_nb_chars=127)
    publish_date    = Faker('data', pattern="%Y-%m-%d")
    journal         = SubFactory(JournalFactory)
