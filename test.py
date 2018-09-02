# Test sqlalchemy model
from flask_app import application
from application import db
from flask_app.application import models

Journal = models.Journal
Article = models.Article
Author = models.Author
ArticleURL = models.ArticleURL

app = application.create_app('development')
app.app_context().push()

def test_db():
    try:
        db.session.query("1").from_statement("SELECT 1").all()
        print('It works')
    except:
        return print('Something is broken')

def test_journal(name, url, issn_p, issn_o):
    j = Journal(
        journal_name = name,
        journal_url = url,
        issn_print = issn_p,
        issn_online = issn_o
        )
    db.session.add(j)
    db.session.commit()

    our_journal = db.session.query(Journal).filter_by(issn_print=issn_p)

    assert our_journal.__tablename__ == 'gigmc_journals'
    assert repr(our_journal) == "<Journal(Name = %s )>," % (name)

def test_article(name, date, j_id):
    a = Article(
        article_name = name,
        publish_date = date,
        fk_journal_id = j_id
    )
    db.session.add(a)
    db.session.commit()

    our_article = db.session.query(Article).filter_by(article_name=name)

    assert our_article.__tablename__ == 'gigmc_articles'
    assert repr(our_article) == "<Article(Title = %s )>," % (name)

def test_author(first, last):
    a = Author(first_name = first, last_name = last)

    db.session.add(a)
    db.session.commit()

    our_author = db.session.query(Author).filter_by(last_name=last)

    assert our_author.__tablename__ == 'gigmc_authors'
    assert repr(our_author) == "<Author(Full Name=%s %s)>" % (
            first, last)

def test_url(url, article):
    u = ArticleURL(article_url=url, fk_article_id=article)

    db.session.add(u)
    db.session.commit()

    our_url = db.session.query(ArticleURL).filter_by(article_url=url)

    assert our_url.__tablename__ == 'gigmc_links'
