# -*- coding: utf-8 -*-
"""
    tests.factory
    ~~~~~~~~~~~~~~~

    Factories for test fixture data
"""

from factory import SubFactory, Faker, alchemy, Sequence, LazyAttribute
from application.models import Journal, Article, Author, ArticleURL
from tests.setup import Session

class AppFactory(alchemy.SQLAlchemyModelFactory):

    sqlalchemy_session              = Session
    sqlalchemy_session_persistence  = 'commit'

class JournalFactory(AppFactory):
    class Meta:
        model       = Journal

    journal_name    = Faker('bs')
    journal_url     = Faker('url')
    issn_print      = Faker('ean', length=8)
    issn_online     = Faker('ean', length=8)


class ArticleFactory(AppFactory):
    class Meta:
        model       = Article

    article_name    = Faker('text', max_nb_chars=127)
    publish_date    = Faker('data', pattern="%Y-%m-%d")
    journal         = SubFactory(JournalFactory)
