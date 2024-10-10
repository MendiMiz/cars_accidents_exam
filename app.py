from flask import Flask
from routes.area_controller import area_blueprint


def create_app():
    flask_app = Flask(__name__)
    flask_app.register_blueprint(area_blueprint, url_prefix="/api/area")
    return flask_app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)