from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()

def create_app(**config_overrides):
    app = Flask(__name__)

    # Load config
    app.config.from_pyfile('settings.py')

    # apply overrides for tests
    app.config.update(config_overrides)

    # Initialize db
    db.init_app(app)
    migrate = Migrate(app, db)

    from counter.views import counter_app

    app.register_blueprint(counter_app)

    return app