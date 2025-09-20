from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

db = SQLAlchemy()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object("backend.config.Config")

    db.init_app(app)
    jwt.init_app(app)

    # register blueprints
    from .routes import auth_bp, protected_bp
    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(protected_bp, url_prefix="/api")

    # create DB tables if not exist
    with app.app_context():
        db.create_all()

    return app
