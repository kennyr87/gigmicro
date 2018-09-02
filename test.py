# Test sqlalchemy model

def test_db():
    try:
        db.session.query("1").from_statement("SELECT 1").all()
        print('It works')
    except:
        return print('Something is broken')

def test_journal_model_class(name, url, issn_p, issn_o):
    j = Journal(
        journal_name = name,
        journal_url = url,
        issn_print = issn_p,
        issn_online = issn_o
        )
    db.session.add(j)
    db.session.commit()

    our_journal = db.session.query(Journal).filter_by(issn_print=issn_p)

    assertTrue(j is our_journal)
    assert our_journal.__tablename__ == 'gigmc_journals'
    assert repr(our_journal) == "<Journal(Name = %s )>," % (name)

def test_article_model_class(name, date, j_id):
    a = Article(
        article_name = name,
        publish_date = date,
        fk_journal_id = j_id
    )
    db.session.add(a)
    db.session.commit()

    our_article = db.session.query(Article).filter_by(article_name=name)

    assertTrue(a is our_article)
    assert our_article.__tablename__ == 'gigmc_articles'
    assert repr(our_article) == "<Article(Title = %s )>," % (name)

def test_author_model_class(first, last):
    a = Author(first_name = first, last_name = last)

    db.session.add(a)
    db.session.commit()

    our_author = db.session.query(Author).filter_by(last_name=last)

    assertTrue(a is our_auth)
    assert our_article.__tablename__ == 'gigmc_authors'
    assert repr(our_author) == "<Author(Full Name=%s %s)>" % (
            first, last)

def test_url_model_class(url, article):
    u = ArticleURL(article_url=url, fk_article_id=article)

    db.session.add(u)
    db.session.commit()

    our_url = db.session.query(ArticleURL).filter_by(article_url=url)

    assertTrue(u is our_url)
    assert our_url.__tablename__ == 'gigmc_links'
