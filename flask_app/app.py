# -*- coding: utf-8 -*-
"""
    flask_app.app
    ~~~~~
    application entry point
"""

import os
from .factory import create_app

config_name = os.getenv('FLASK_CONFIG')

app = create_app(config_name)

if __name__ == "__main__":
    app.run()
