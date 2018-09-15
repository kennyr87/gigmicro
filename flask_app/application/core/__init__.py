from . import core
from application.models import Author, Journal, Article, ArticleURL

class URLService(Service):
    __model__       = ArticleURL

class ArticleService(Service):
    """
    Interface to Article Model
    """
    __model__       = Article

    def __init__(self):
        super().__init__()
        self.article_url    = URLService()

class AuthorService(Service):
    """
    Interface to Author model
    """
    __model__       = Author

class JournalService(Service):
    """
    Interface to Journal model
    """
    __model__       = Journal
