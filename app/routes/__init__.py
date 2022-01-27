from flask import Blueprint, Flask
from app.routes.series_route import bp_series

bp_api = Blueprint("api", __name__, url_prefix="/api")

def init_app(app: Flask):
    
    bp_api.register_blueprint(bp_series)
    app.register_blueprint(bp_api)