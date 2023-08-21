from app import create_app, db
from config.settings import Config

app = create_app(Config)

if __name__ == '__main__':
    app.run()
