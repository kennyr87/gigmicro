# -*- coding: utf-8 -*-
"""
    tests.settings
    ~~~~~~~~~~~~~~

    tests settings module
"""

SOCKET = '?unix_socket=/var/run/mysqld/mysqld.sock' 
SQLALCHEMY_DATABASE_URI = 'mysql+mysqldb://root@localhost/gigmicro' + SOCKET
