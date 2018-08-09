from flask_app import create_app

app = create_app('flask_app.application.settings.ProdConfig')

if __name__ == "__main__":

    app.run()
