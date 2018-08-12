from application import create_app
from flask_app import settings

app = create_app('settings.ProdConfig')

if __name__ == "__main__":
    app.run()
