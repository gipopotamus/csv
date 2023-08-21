from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config.settings import Config

db = SQLAlchemy()
migrate = Migrate()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)  # Инициализация Flask-Migrate

    with app.app_context():
        db.create_all()

    from app.routes import bp as api_bp
    app.register_blueprint(api_bp, url_prefix='/api')

    return app
