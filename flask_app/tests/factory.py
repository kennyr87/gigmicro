# -*- coding: utf-8 -*-
"""
    tests.factory
    ~~~~~~~~~~~~~~~

    Factories for test fixture data
"""

from factory import SubFactory, Faker, alchemy, Sequence, LazyAttribute
from application.models import Journal, Article, Author, ArticleURL
from tests import Session

class JournalFactory(alchemy.SQLAlchemyModelFactory):
    class Meta:
        model               = Journal
        sqlalchemy_session  = Session

        journal_name    = Faker('bs')
        journal_url     = Faker('url')
        issn_print      = Faker('ean', length=8)
        issn_online     = Faker('ean', length=8)


class ArticleFactory(alchemy.SQLAlchemyModelFactory):
    class Meta:
        model               = Article
        sqlalchemy_session  = Session

        article_name    = Faker('text', max_nb_chars=127)
        publish_date    = Faker('data', pattern="%Y-%m-%d")
        journal         = SubFactory(JournalFactory)
