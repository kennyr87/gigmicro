# from application import db
# from sqlalchemy import db.Column, Index, ForeignKey, Table
# from sqlalchemy.dialects.mysql import db.MEDIUMINT, db.VARCHAR, CHAR, DATE

# map classes to database tables

class Journal(db.Model):
    __tablename__ = 'gigmc_journals'

    jounrnal_id = db.Column(db.MEDIUMINT, primary_key=True)
    journal_name = db.Column(db.VARCHAR(127), nullable=False)
    journal_url = db.Column(db.VARCHAR(255))
    issn_print = db.Column(db.CHAR(8), unique=True)
    issn_online = db.Column(db.CHAR(8), unique=True)

    journal_articles = relationship("Article")

class Article(db.Model):
    __tablename__ = 'gigmc_articles'

    article_id = db.Column(db.MEDIUMINT, primary_key=True)
    article_name = db.Column(db.VARCHAR(127), nullable=False)
    publish_date = db.Column(db.DATE, nullable=False)
    fk_journal_id = db.Column(
        db.MEDIUMINT,
        db.ForeignKey("gigmc_journals.journal_id"),
        nullable=False)

    article_links = db.relationship("ArticleURL")

    def __repr__(self):
        return "<Article(Title='%s', Publish Date='%s')>" % (
            self.article_name, self.publish_date)

class Author(db.Model):
    __tablename__ = 'gigmc_authors'

    author_id = db.Column(db.MEDIUMINT, primary_key=True)
    first_name = db.Column(db.VARCHAR(31))
    middle_initial = db.Column(CHAR(1))
    last_name = db.Column(db.VARCHAR(31), nullable=False)

    __table_args__ = (
        db.Index('idx_lf_name', 'last_name', 'first_name'),
        )

    articles = db.relationship(
        "Article",
        secondary=author_article_assoc,
        backref="authors",
        passive_deletes=True)

    def __repr__(self):
        return "<Author(Full Name='%s' '%s')>" % (
            self.first_name, self.last_name)

class ArticleURL(db.Model):
    __tablename__ = 'gigmc_links'

    link_id = db.Column(db.MEDIUMINT, primary_key=True)
    article_url = db.Column(db.VARCHAR(255), nullable=False)
    fk_article_id = db.Column(
        db.MEDIUMINT,
        db.ForeignKey("gigmc_articles.article_id"),
        nullable=False)

    def __repr__(self):
        return "<URL(Link='%s', Name='%s')>" % (
            self.article_url, gigmc_articles.article_name)

# Association table for author to article bidirectional relationship
author_article_assoc = db.Table('gigmc_author_article', db.Model.metadata,
    db.Column('id', db.MEDIUMINT, primary_key=True),
    db.Column('fk_author_id',
        db.MEDIUMINT,
        db.ForeignKey("gigmc_authors.author_id"),
        nullable=False),
    db.Column('fk_article_id',
        db.MEDIUMINT,
        db.ForeignKey("gigmc_articles.article_id"),
        nullable=False)
)
