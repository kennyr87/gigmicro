from application import (
    create_app,
    settings
)

app = create_app('application.settings.ProdConfig')

if __name__ == "__main__":
    app.run()
