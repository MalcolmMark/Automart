from flask import Flask

from .config import Config
from .extensions import db
from .routes.auth import auth_bp
from .routes.listings import listings_bp


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)

    with app.app_context():
        db.create_all()

    app.register_blueprint(auth_bp, url_prefix="/api/auth")
    app.register_blueprint(listings_bp, url_prefix="/api/listings")

    @app.get("/health")
    def health():
        return {"status": "ok"}, 200

    return app
