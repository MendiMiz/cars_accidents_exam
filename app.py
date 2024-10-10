from flask import Flask
from routes.area_controller import area_blueprint
from routes.init_controller import db_blueprint


def create_app():
    flask_app = Flask(__name__)
    flask_app.register_blueprint(area_blueprint, url_prefix="/api/area")
    flask_app.register_blueprint(db_blueprint, url_prefix="/api/db")
    return flask_app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)