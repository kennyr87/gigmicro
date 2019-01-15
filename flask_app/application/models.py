"""
    application.models
    ~~~~~~~~~~~~~~~~~~

    SQL Alchemy models
"""

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.mysql import MEDIUMINT
from ..helpers import JsonSerializer

db = SQLAlchemy()

# Association table for author to article bidirectional relationship
author_article_assoc    = db.Table('gigmc_author_article', db.Model.metadata,
    db.Column('id', MEDIUMINT, primary_key=True),
    db.Column('fk_author_id',
        MEDIUMINT,
        db.ForeignKey("gigmc_authors.author_id"),
        nullable=False),
    db.Column('fk_article_id',
        MEDIUMINT,
        db.ForeignKey("gigmc_articles.article_id"),
        nullable=False)
)

class JournalJsonSerializer(JsonSerializer):
    __json_hidden__     = ['journal_articles']

# map classes to database tables
class Journal(JournalJsonSerializer, db.Model):
    __tablename__       = 'gigmc_journals'

    journal_id          = db.Column(MEDIUMINT, primary_key=True)
    journal_name        = db.Column(db.VARCHAR(127), nullable=False)
    journal_url         = db.Column(db.VARCHAR(255))
    issn_print          = db.Column(db.CHAR(8), unique=True)
    issn_online         = db.Column(db.CHAR(8), unique=True)

    journal_articles    = db.relationship("Article", backref='journal')

    def __repr__(self):
        return "<Journal(Name = %s)>" % (
            self.journal_name)

class Article(db.Model):
    __tablename__   = 'gigmc_articles'

    article_id      = db.Column(MEDIUMINT, primary_key=True)
    article_name    = db.Column(db.VARCHAR(127), nullable=False)
    publish_date    = db.Column(db.DATE, nullable=False)
    fk_journal_id   = db.Column(
        MEDIUMINT,
        db.ForeignKey("gigmc_journals.journal_id"),
        nullable=False)

    article_links   = db.relationship("ArticleURL", backref='article')

    def __repr__(self):
        return "<Article(Title = %s)>" % (
            self.article_name)

class Author(db.Model):
    __tablename__   = 'gigmc_authors'

    author_id       = db.Column(MEDIUMINT, primary_key=True)
    first_name      = db.Column(db.VARCHAR(31))
    middle_initial  = db.Column(db.CHAR(1))
    last_name       = db.Column(db.VARCHAR(31), nullable=False)

    __table_args__  = (
        db.Index('idx_lf_name', 'last_name', 'first_name'),
        )

    articles            = db.relationship(
        "Article",
        secondary       = author_article_assoc,
        backref         = "authors",
        passive_deletes = True)

    def __repr__(self):
        return "<Author(Full Name=%s %s)>" % (
            self.first_name, self.last_name)

class ArticleURL(db.Model):
    __tablename__   = 'gigmc_links'

    link_id         = db.Column(MEDIUMINT, primary_key=True)
    article_url     = db.Column(db.VARCHAR(255), nullable=False)
    fk_article_id   = db.Column(
        MEDIUMINT,
        db.ForeignKey("gigmc_articles.article_id"),
        nullable=False)

    def __repr__(self):
        return "<URL(Link='%s', Name='%s')>" % (
            self.article_url, gigmc_articles.article_name)
