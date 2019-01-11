# -*- coding: utf-8 -*-
"""
    tests.settings
    ~~~~~~~~~~~~~~

    tests settings module
"""
from sqlalchemy.orm import scoped_session, sessionmaker

SOCKET = '?unix_socket=/var/run/mysqld/mysqld.sock' 
SQLALCHEMY_DATABASE_URI = 'mysql+mysqldb://root@localhost/gigmicro' + SOCKET
SESSION = scoped_session(sessionmaker())